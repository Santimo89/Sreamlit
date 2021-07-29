

import streamlit as st
from PIL import Image
from src.support.py import load_data



st.write("""
# Prediciones Surf
""")

st.text(""" The main objetive of this proyect is to predict according to some variables the best month to go surfing to the nort of Spain and where to go""")


col1, col2 = st.beta_columns(2)
with col1:
    image = Image.open("C:\Users\santi\OneDrive\Escritorio\Surf pic.jpg")
    st.image(image, use_column_width = True)

with col2:
    image = Image.open("C:\Users\santi\OneDrive\Escritorio\Sol RIba.jpg")
    st.image(image, use_column_width = True)



st.write(""" ### Beach list to go surfing
""")

x = load_data


st.table


