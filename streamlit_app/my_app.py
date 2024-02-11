import streamlit as st
import requests


from textfile_app import *
from get_data import Image, str_to_date
from src.enums.global_enums import WrongStatusCode
from class_streamlit import Streamlit 
from image_editor import Editor


stream = Streamlit()

stream.make_title(header)

with st.sidebar:

    # Ввод данных
    with st.form("Форма1"):
        stream.make_subheader("Введите данные для запроса на сервер")
        long = stream.make_input_number(long_label, 95.21, -180.0, 180.0)
        lat = stream.make_input_number(lat_label, 29.67, -90.0, 90.0)

        date = stream.make_input_date(date_label, "2018-07-01", "1995-06-16", "2023-07-01")

        submitted = stream.make_form_but("Получить изображение")
    
    



try:

    # Отображаем полчченную картинку
    dataset = Image(long, lat,  date)
    image = dataset.download_image('image')

    stream.make_subheader("Полученное изображение:")
    name = stream.make_post_image(image)

    # Открываем редактировани только после загрузки полученного изображения
    if name:

        

        # Обработка изображений 
        with st.form("Форма2"):
            stream.make_subheader("Как вы хотите изменить изображение?")
            
            # Функции
            color = stream.male_slider(color_label, 0.0, 2.0, 1.0)
            contrast = stream.male_slider(contrast_label, 0.0, 2.0, 1.0)
            brightness = stream.male_slider(brightness_label, 0.0, 2.0, 1.0)

            # Кнопка отправки данных 
            submitted = stream.make_form_but("Преобразовать изображение")
        
        try:
            edit = Editor(image, color, contrast, brightness)
# 
            edit_image = edit.editing()
            stream.make_post_image(edit_image)

        except Exception as e:
            stream.make_error(edit)


except WrongStatusCode:
    stream.make_error(get)
        

# edit = Editor(image ,0.5, 0.5, 0.5)
# edit_image = edit.editing()