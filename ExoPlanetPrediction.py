import streamlit as st
import numpy as np
import pandas as pd


df = pd.read_csv('exoplanets.csv')
# Create a title
st.title('Exoplanet Classification')

# Add some text
st.text("Using Machine Learning to classify Exoplanets")

# Add an image
# from PIL import Image
# image = Image.open('exoplanets.jpg')
# st.image(image, caption='Exoplanets', use_column_width=True)

# Add a sidebar
st.sidebar.header('User Input Parameters')

st.write("""
## Planety radius [Earth radii]
""")
input_planet_rad = np.float(st.text_input('Enter the observed planets radii'))