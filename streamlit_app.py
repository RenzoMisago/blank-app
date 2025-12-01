import streamlit as st
from PIL import Image

st.title("Display Local Image (No URL Needed)")

image = Image.open("images/hk-logo.jpg")
st.image(image, caption="Local Image from Repository", use_column_width=True)
