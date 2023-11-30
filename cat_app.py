import streamlit as st
import requests

# code to config the page
st.set_page_config(page_title="Cat App", page_icon=":cat:")

st.header("Welcome to my :cat: app!", divider="rainbow")


def get_content():
    # access the API and get the image URL
    contents = requests.get("https://cataas.com//cat")
    return contents.content


def place_cat_image():
    cat_image = get_content()
    st.image(cat_image, width=200)


# add a button
st.button("Click here!", on_click=place_cat_image, help="Click to get a cat image")

