# LangChain POC – Restaurant Name & Menu Generator (Agentic AI Demo)

This project is a small Proof of Concept demonstrating practical skills in **LangChain**, **LLMs**, and **Agentic AI**.

The user enters a cuisine type (ex: Thai / Italian / Indian).  
The system then uses a Hugging Face LLM endpoint to:

- Generate a unique Restaurant Name
- Generate a Custom Restaurant Menu
- Display structured output inside a Streamlit UI

This shows my capability to build runnable LangChain chains, use Hugging Face hosted models, parse responses, and deploy an interactive LLM app.

---

## 🚀 Tech Stack

| Component | Purpose |
|----------|----------|
| Python | Main language |
| LangChain | LLM orchestration workflow |
| HuggingFace | LLM provider (Qwen/Qwen2.5-7B-Instruct) |
| Streamlit | UI layer |

---

## Configure API Keys

Create a .env file inside project root:

HUGGING_FACE_API_KEY=your_hf_token_here

## Run Stream App

streamlit run main.py

App will open at:

http://localhost:8501