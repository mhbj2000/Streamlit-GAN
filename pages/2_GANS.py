import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="GANS Demonstration", layout="wide")

with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
#potential headers
st.header('HEADER')

# ---- SIDE BAR COTNROLS ---- 
with st.container():
    st.sidebar.subheader("CONTROLS")
    left_column, right_column = st.sidebar.columns(2)
    with left_column:
        if st.sidebar.button("Generate GANs"):
            pass
    with right_column:
        if st.sidebar.button("Stop"):
            pass

# ---- GAN Visualizer Row 1 ----         
with st.container():
    # change to gif 1
    real_image_1 = Image.open('Pic/01.jpg')
    #real_image_2 = Image.open('Pic/02.jpg')
    #real_image_3 = Image.open('Pic/03.jpg')
    new_size = (200,200)
    #real_image_1.resize(new_size)
    #real_image_2.resize(new_size)
    #real_image_3.resize(new_size)
    st.write('---')
    st.subheader('idk')
    col1,col2 = st.columns(2)
    with col1:
        st.image(real_image_1)
    with col2:
        st.image(real_image_2)
# ---- GAN Visualizer Row 2 ----       
with st.container():
    st.write('---')
    st.subheader('idk')
    fake_image_1 = Image.open('Pic/Fake_Image_01.png') 
    #fake_image_2 = Image.open('Pic/Fake_Image_02.png') 
    #fake_image_3 = Image.open('Pic/Fake_Image_03.png')  
    new_size=(200,200)
    fake_image_1.resize(new_size)
    #fake_image_2.resize(new_size)
    #fake_image_3.resize(new_size)
    col1,col2 = st.columns(2)
    with col1:
        st.image(fake_image_1)
    with col2:
        pass
        #st.image(fake_image_2)
# ---- GAN Visualizer Row 3 ----       
with st.container():
    st.write('---')
    st.subheader('idk')
    fake_image_1 = Image.open('Pic/Fake_Image_01.png') 
    #fake_image_2 = Image.open('Pic/Fake_Image_02.png') 
    #fake_image_3 = Image.open('Pic/Fake_Image_03.png')  
    new_size=(200,200)
    fake_image_1.resize(new_size)
    #fake_image_2.resize(new_size)
    #fake_image_3.resize(new_size)
    col1,col2 = st.columns(2)
    with col1:
        st.image(fake_image_1)
    with col2:
        st.write('A description of the GIF')

        pass
    
        #st.image(fake_image_2)
