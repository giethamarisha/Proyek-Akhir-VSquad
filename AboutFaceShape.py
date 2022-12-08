import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(
    page_title='Multipage app'
)
st.header("Recommendations for Optical Eyeglass Frames Based on Face Shape")
st.image(f"./image/img faceshape.jpeg", width=800)
st.header('About Face Shape')
st.text("The shape of each person's face is different enough to have an impact on appearance")
st.text("For example, someone who wants to buy glasses will certainly adjust the model of")
st.text("glasses that match the shape of the face they have")
st.sidebar.success('select a page above')