import datetime
import streamlit as st


st.title('Kaiken form')
st.caption('create a profile for your Kai')

col1, col2 = st.columns(2)

with col1:
    with st.form(key='profile_form'):
        name = st.text_input('name')
        sex_female = st.checkbox('female')
        sex_male = st.checkbox('male')
        age = st.number_input('age', value=0)
        birthday = st.date_input(
        "When's your birthday",
        datetime.date(2022, 7, 6))
        body_type = st.selectbox(
            'body type',
            ('猪型 : inoshishi-kata', '鹿型 : shika-kata')
        )
        color = st.multiselect(
            'color',
            ('黒虎 : kuro-tora', '中虎 : chu-tora', '赤虎 : aka-tora')
        )
        tail = st.radio(
            'tail type',
            ('差尾 : sashi-o', '巻尾 : maki-o')
        )
        energy_level = st.slider('energy level', min_value=0, max_value=10)
        
        txt = st.text_area(
            'Add anything about your baby',
            placeholder='My baby is...'
        )
        
        submit_btn = st.form_submit_button('Submit')
    
    
    with col2:
        
        if submit_btn:
            st.subheader(f"Your baby's name is {name}")
            # st.text(f'Name: {name}')
            st.text(f'age: {age}')
            st.text(f'birthday: {birthday}')
            if sex_female == True: 
                st.text('sex: female')
            elif sex_male == True:
                st.text('sex: male') 
            st.text(f'body type: {body_type}')
            st.text(f'color: {"".join(color)}')
            st.text(f'tail: {tail}')
            st.text(f'energy level: {energy_level}')
            st.write(f'description:', {"".join(txt)})

