import datetime
from PIL import Image
import streamlit as st

st.title('Kaiken')
st.caption('Japanese breed 一代一主')
st.subheader('Simple Kaiken profile form')

image = Image.open('./data/kaiyamato.JPG')
st.image(image, width=500)

st.text("The Kai Ken (甲斐犬, also called the Tora Inu or Tiger Dog) is a breed of dog from Japan.\nIt is a rare dog even in its native land\nand is one of the six native Japanese dog breeds protected by the Nihon Ken Hozonkai.")