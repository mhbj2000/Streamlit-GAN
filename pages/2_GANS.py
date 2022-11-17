import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="GANS Demonstration", layout="wide")

with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
#potential headers
st.header('GAN VISUALIZER')
rain_timelapse_counter = 4
fog_timelapse_counter = 4

# ---- SIDE BAR COTNROLS ---- 
#with st.container():
    #st.sidebar.subheader("CONTROLS")
    #left_column, right_column = st.sidebar.columns(2)
    #with left_column:
        #rain_counter = st.slider('Timelapses', 0,19,4)
        #if st.sidebar.button("View Next Rain Timelapse"):
            #rain_timelapse_counter = rain_timelapse_counter + 1
            #st.write(rain_timelapse_counter)
    #with right_column:
        #if st.sidebar.button("View Next Fog Timelapse"):
            #fog_timelapse_counter =+1

# ---- GAN Rain Visualizer | Row 1 ----         
with st.container():
    st.write('---')
    st.subheader('Clear to Rain Model')
    col1,col2,col3 = st.columns(3)
    with col3: #CONTROLS FOR THE ENTIRE ROW
        model_selector = st.selectbox('Choose an image to run.',('Example 1', 'Example 2', 'Example 3'))
        if model_selector == 'Example 1':
            rain_counter = st.slider('GAN Iteration', 40,49,40)
            rain_timelapse_picture = Image.open('IntermediatePic/RainFake/Fake4/False_image_'+str(rain_counter)+'.png')
            image_resizer = (400,400)
            rain_timelapse_picture = rain_timelapse_picture.resize(image_resizer)
            rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse4.mp4', 'rb')
            video_bytes = rain_timelapse.read()
        elif model_selector == 'Example 2':
            #rain_counter = st.slider('GAN Iteration',
            rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse7.mp4', 'rb')
            video_bytes = rain_timelapse.read()
            
        
        #rain_counter = st.slider('GAN Iteration', 40,49,40)
        #rain_timelapse_picture = Image.open('IntermediatePic/RainFake/Fake4/False_image_'+str(rain_counter)+'.png')
        #image_resizer = (400,400)
        #rain_timelapse_picture = rain_timelapse_picture.resize(image_resizer)
        #rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse4.mp4', 'rb')
        #video_bytes = rain_timelapse.read()
        st.write('Length of Clear Dataset: 1013 Images  \n',
                 'Length of Rainy Dataset: 1054 Images  \n',
                 'Time to Train: 10:30 Hours')
    with col1:
        #st.video(video_bytes)
        #st.image(rain_timelapse_picture)
        st.video(video_bytes)
        
        pass
    with col2:
        st.image(rain_timelapse_picture)
        
# ---- GAN Visualizer Row 2 ----       
with st.container():
    st.write('---')
    st.subheader('Clear to Fog Model')
    col1,col2 = st.columns(2)
    with col2:
        fog_counter = st.slider('Fog Timelapses', 0,19,4)
        fog_timelapse = open('Time-lapse/FogTimelapse/Timelapse'+str(fog_counter)+'.mp4', 'rb')
        fog_bytes = fog_timelapse.read()
        st.write('Length of Clear Dataset: 1013 Images  \n',
        'Length of Fog Dataset: 1008 Images  \n',
        'Time to Train: 10:30 Hours')
    with col1:
        st.video(fog_bytes)
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
