import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="GANS Demonstration", layout="wide")

with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
#potential headers
st.header('GAN VISUALIZER')

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

# ---- GAN Rain Visualizer | Row 1 ----         
with st.container():
    # change to gif 1
    rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse4.mp4', 'rb')
    video_bytes = rain_timelapse.read()
    real_image_1 = Image.open('Pic/01.jpg')
    #real_image_2 = Image.open('Pic/02.jpg')
    #real_image_3 = Image.open('Pic/03.jpg')
    new_size = (200,200)
    #real_image_1.resize(new_size)
    #real_image_2.resize(new_size)
    #real_image_3.resize(new_size)
    st.write('---')
    st.subheader('Clear to Rain Model')
    col1,col2 = st.columns(2)
    with col1:
        #st.image(real_image_1)
        st.video(video_bytes)
    with col2:
        st.write('Length of Clear Dataset: 1013 Images  \n',
                 'Length of Rainy Dataset: 1054 Images  \n',
                 'Time to train: 10:30 Hours')
        pass
        #st.image(real_image_2)
# ---- GAN Visualizer Row 2 ----       
with st.container():
    st.write('---')
    st.subheader('Clear to Fog Model')
    fog_timelapse = open('Time-lapse/FogTimelapse/Timelapse4.mp4', 'rb')
    fog_bytes = fog_timelapse.read()
    fake_image_1 = Image.open('Pic/Fake_Image_01.png') 
    #fake_image_2 = Image.open('Pic/Fake_Image_02.png') 
    #fake_image_3 = Image.open('Pic/Fake_Image_03.png')  
    new_size=(200,200)
    fake_image_1.resize(new_size)
    #fake_image_2.resize(new_size)
    #fake_image_3.resize(new_size)
    col1,col2 = st.columns(2)
    with col1:
        #st.image(fake_image_1)
        st.video(fog_bytes)
    with col2:
        st.write('Description')
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
