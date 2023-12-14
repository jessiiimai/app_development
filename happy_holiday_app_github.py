import streamlit as st

# code to config the page
st.set_page_config(page_title="Holiday App", page_icon=":snowman:")

# heading
st.header("GOOD LUCK AND HAPPY HOLIDAYS", divider="rainbow")

# add an image
file_path = "image/frozen-olaf.jpg"
st.image(file_path, caption="Happy Holidays!")
