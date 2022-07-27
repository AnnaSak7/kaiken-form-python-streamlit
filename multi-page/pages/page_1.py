
import streamlit as st
from PIL import Image

st.title('My Kais')
st.subheader('Kaiya')

st.text(f'Name: Kaiya')
st.text(f'age: 8')
st.text(f'birthday: 2014-6-14')
st.text(f'sex: female')
st.text(f'body type: 猪型 : inoshishi-kata')
st.text(f'color: 黒虎 : kuro-tora')
st.text(f'tail: 巻尾 : maki-o')
st.text(f'energy level: 5')

kaiya_image = Image.open('./data/kaiya.JPG')
st.image(kaiya_image, width=500)
st.text('Kaiya is a girl who was born in June, 2014 in Japan\nand came to Sweden when she was 2 months old.\nShe has a inoshishi body type like her father\nand maki-o, curly tail like her mother.')
