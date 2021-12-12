import streamlit as st
from PIL import Image

#import seaborn as sns
#import pandas as pd 
#import numpy as np

img=Image.open("yo.jpeg")
st.image(img,width=100)

if st.button("Saludame"):    
    st.markdown("Me llamo Mari, y te la bienvenida a mi pagina streamlit")
    #Ballons
    st.balloons()

st.markdown("# MariChat")
st.markdown("*Un chatbot para preguntar sobre programación in Python*")

st.text_area("usuario", value="", height=None, max_chars=None, key=None, help="escribe tu pregunta aquí")

