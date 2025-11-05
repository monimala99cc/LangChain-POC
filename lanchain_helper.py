from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap  # <-- key fix
from operator import itemgetter
import re

from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("HUGGING_FACE_API_KEY")

llm = ChatOpenAI(       #using CharOpenAI instead of InferenceClient,because InferenceClient is not runnable
    api_key=token,
    base_url="https://router.huggingface.co/v1",
    model="Qwen/Qwen2.5-7B-Instruct",
    temperature=0.6,
)
def extract_name(text):
    name = re.search(r'"(.*?)"', text).group(1)
    return name

def extract_menu(text):
    match = re.search(r'([A-Z][\w\s]+?)\s+Menu.*', text, re.DOTALL)
    if match:
        result = match.group(0)
    return result


def generate_restaurant_name(cuisine):
    # first chain

    prompt_name = PromptTemplate(
        input_variable=['cuisine'],
        template="I want to open an {cuisine} restaurant. Give me a unique name"
    )

    chain_restra_name = prompt_name | llm | StrOutputParser()  # RunnableSequence

    # second chain: restraurant menu

    prompt_menu = PromptTemplate(
        input_variable=['restaurant_name'],
        template="I want to open an restaurant named: {restaurant_name}. Can you create a restaurant menu."
    )
    chain_restra_menu = prompt_menu | llm | StrOutputParser()

    # compose like SequentialChain (multiple inputs, keep intermediates)
    chain = (
            RunnableMap({
                "cuisine": itemgetter("cuisine"),  # pass-through
                "restaurant_name": chain_restra_name,  # uses {cuisine}
            })
            | RunnableMap({
        "restaurant_name": itemgetter("restaurant_name"),
        "cuisine": itemgetter("cuisine"),
        "menu": chain_restra_menu,
    })
    )

    response = chain.invoke({"cuisine": cuisine})
    return response
