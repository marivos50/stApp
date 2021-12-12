import streamlit as st
from PIL import Image

#import seaborn as sns
#import pandas as pd 
#import numpy as np


st.markdown("# stApp")
st.markdown("Explore the dataset to know more about palmerpenguins")
img=Image.open("yo.jpeg")
st.image(img,width=100)
st.markdown("**Marichat** Un chatbot para preguntar sobre programación in Python")
st.text_area("usuario", value="", height=None, max_chars=None, key=None, help="escribe tu pregunta aquí")
if st.button("Saludame"):    
    st.markdown("Me llamo Mari, y te doy un beso de bienvenida a mi pagina streamlit")
    #Ballons
    st.balloons()
