import streamlit as st
import requests


from textfile_app import *
from get_data import Image, str_to_date
from src.enums.global_enums import WrongStatusCode
from class_streamlit import Streamlit 

st.title(header, help=None)

# dataset = Image(106.21, 29.67, '2018-07-01')
# image = dataset.download_image('image')
# st.image(image=image, caption='Спутниковый снимок')

# Задаём параметры для кнопки



if 'count' not in st.session_state:
    st.session_state.count = 0


def change_input_lat(data):
    # data.append()
    pass

def change_input_long(data):
    # data.append()
    pass

stream = Streamlit()

with st.sidebar:
    with st.form("Форма"):

        stream.make_subheader("Введите данные для запроса на сервер")
        long = stream.make_input_number(long_label, 95.21, -180.0, 180.0)
        lat = stream.make_input_number(lat_label, 29.67, -90.0, 90.0)

        date = stream.make_input_date(date_label, "2018-07-01", "1995-06-16", "2023-07-01")

        submitted = stream.make_form_but("Получить изображение")

try:

    dataset = Image(long, lat,  date)
    image = dataset.download_image('image')
    stream.make_post_image(image)

except WrongStatusCode:
    stream.make_error(text)
        

    

# 
# 
# try:
# 
    # dataset = Image(long, lat,  date)
    # image = dataset.download_image('image')
    # stream.post_image(image)
# 
# except WrongStatusCode:
    # st.write(text)