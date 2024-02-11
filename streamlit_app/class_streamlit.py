import streamlit as st

from get_data import str_to_date

class Streamlit():
    """
    Класс для работы с библиотекой streamlit. 
    Создан лдя того, чтобы не загромождать главный файл приложения
    """

    def __init__(self) -> None:
        pass

    def make_title(self, text):
        name = st.title(body=text)
        return name
    
    def make_subheader(self, text):
        name = st.subheader(body=text)
        return name
    
    def make_error(self, text):
        name = st.error(body=text)
        return name

    def make_input_number(self, label, value, min_value, max_value):
        name = st.number_input(label=label,value=value, min_value=min_value, max_value=max_value)
        return name

    def make_input_date(self, label, value, min_value, max_value):
        name = st.date_input(label=label,value=str_to_date(value), min_value=str_to_date(min_value), max_value=str_to_date(max_value))
        return name
    
    def make_post_image(self, image):
        name = st.image(image)
        return name
    
    def make_form_but(self, label):
        name = st.form_submit_button(label)
        return name
    
    def male_slider(self, label, minimum, maximum, standart):
        name = st.slider(label=label, min_value=minimum, max_value=maximum, value=standart)    
