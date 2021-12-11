# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 15:35:45 2021

@author: Mari
"""

import streamlit as st
from PIL import Image

#import seaborn as sns
#import pandas as pd 
#import numpy as np

DATA_URL = ("penguins.csv")

st.markdown("# Self Exploratory Visualization on palmerpenguins")
st.markdown("Explore the dataset to know more about palmerpenguins")
img=Image.open('penguin.PNG')
st.image(img,width=100)
st.markdown("**Penguins** are some of the most recognizable and beloved birds in the world and even have their own holiday: **World Penguin Day is celebrated every year on April 25**. Penguins are also amazing birds because of their physical adaptations to survive in unusual climates and to live mostly at sea. Penguins propel themselves through water by flapping their flippers. Bills tend to be long and thin in species that are primarily fish eaters, and shorter and stouter in those that mainly eat krill.")
st.markdown("The data presented are of 3 different species of penguins - **Adelie, Chinstrap, and Gentoo,** collected from 3 islands in the **Palmer Archipelago, Antarctica.**")

if st.button("Saludame"):
    img=Image.open('yo.jpeg')
    st.image(img,width=700, caption="Te saludo")
    st.markdown("Me llamo Mari, y te doy un beso de bienvenida a mi pagina streamlit")
    #Ballons
    st.balloons()

