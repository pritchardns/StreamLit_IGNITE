import streamlit as st
import pandas as pd 
import numpy as np
from PIL import Image


with st.sidebar:
  image = Image.open("IgniteLogo-Letters.png")
  st.image(image)
  st.header('Live Scores')
  st.selectbox('Select Meet', ['ACTTI', 'PPC - WAG','PPC - MAG','PPC - USAG T&T'])
  st.selectbox('Select Session', ['Session 1', 'Session 2'])
  st.selectbox('Select Competition Group', ['Level 7 - 10U - M', 'Level 7 11+ - F'])
  st.text_input('Search by Athlete Name')

    

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
 st.header("A dog")
 st.image("https://static.streamlit.io/examples/dog.jpg", width=200)


with tab2:
 st.header("A dog")
 st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg", width=200)


