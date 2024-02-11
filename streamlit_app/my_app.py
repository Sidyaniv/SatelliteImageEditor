import streamlit as st
import requests

from textfile_app import *
# from get_data import Image

st.title(header, help=None)

# st.image('image.jpeg')



with st.sidebar:
    # st.image()
    lat = st.number_input(lat_label)
    long = st.number_input(long_label)
    print(lat, long)

    date = []
    date_from = st.date_input(label=date_label['first'], min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None)
    date_until = st.date_input(label=date_label['second'], min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None)

    date.append(date)

    st.button(button, use_container_width = True)