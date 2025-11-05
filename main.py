import streamlit as st
import lanchain_helper
st.title("Restaurant Name Generator")

cuisine=st.sidebar.selectbox(" Pick a cuisine",("Indian","French","Mexican","Thai","Syrian"))

if cuisine:
    response=lanchain_helper.generate_restaurant_name(cuisine)
    restra_name=lanchain_helper.extract_name(response['restaurant_name'])
    st.header(restra_name)
    menu= lanchain_helper.extract_menu(response['menu'])
    menu_items=menu.strip().split(",")

    st.write("**Menu Items**")

    for item in menu_items:
        st.write("--",item)