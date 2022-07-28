
import streamlit as st
from PIL import Image

st.title('My Kais')
st.subheader('Mato')

st.text(f'Name: Mato')
st.text(f'age: 6')
st.text(f'birthday: 2016-6-25')
st.text(f'sex: male')
st.text(f'body type: 鹿型 : shika-kata')
st.text(f'color: 黒虎 : kuro-tora')
st.text(f'tail: 差尾 : sashi-o')
st.text(f'energy level: 5')

mato_image = Image.open('./data/mato.JPG')
st.image(mato_image, width=500)
st.text('Mato is a boy who was born in June, 2016 in Japan\nand came to Sweden when he was 4-months old.\nHe is a bit bigger than Kaiya\nand has a slender body like his mother.')
