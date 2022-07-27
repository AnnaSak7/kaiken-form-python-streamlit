import datetime
from PIL import Image
import streamlit as st

st.title('Kaiken')
st.caption('Japanese breed 一代一主')
st.subheader('Simple Kaiken profile form')

image = Image.open('./data/kaiyamato.JPG')
st.image(image, width=500)

