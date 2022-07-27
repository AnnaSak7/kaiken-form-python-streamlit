import datetime
from faulthandler import cancel_dump_traceback_later
from PIL import Image
import streamlit as st

st.title('Streamlit Tutorial')
st.caption('A simple demo of Streamlit')
st.subheader('This is a subheader')
st.text('This is a text\n'
        'This is a text the second line\n')

code = '''
import streamlit as st

st.title('Streamlit App')
'''
st.code(code, language='python')


# video
video_file = open('geometric.mp4', 'rb')
video_bytes =video_file.read()
st.video(video_bytes)

# within with statement, the page does not refresh automatically by just moving cursor unless pressing the button
with st.form(key='profile_form'):
    # textbox
    name = st.text_input('name')
    address = st.text_input('address')
    print(name)
    
    # select box
    age_category = st.selectbox(
        'age category',
        ('<18', '18-24', '25-34', '35-44', '45-54', '>54')
    )
    # radio button
    sex_category = st.radio(
        'sex category',
        ('female', 'male', 'other')
    )
    
    # multiple choice
    hobby = st.multiselect(
        'hobby',
        ('sports', 'photography', 'programming', 'anime', 'movies', 'cocking', 'reading')
    )
    
    # checkbox
    mail_subscribe = st.checkbox('subscribe mail letter')

    # slider
    height = st.slider('height', min_value=110, max_value=210)

    # date
    birthday = st.date_input(
     "When's your birthday",
     datetime.date(2022, 7, 6))
    
    # color picker
    color = st.color_picker('color theme', '#00DAF9')
    
    # button
    submit_btn = st.form_submit_button('Submit')
    cancel_btn = st.form_submit_button('Cancel')
    if submit_btn:
        st.text(f'Welcome! {name}! You are from {address}')
        st.text(f'age: {age_category}')
        st.text(f'sex: {sex_category}')
        st.text(f'hobby: {", ".join(hobby)}')

print(f'submit_btn: {submit_btn}')
print(f'cancel_btn: {cancel_btn}')
