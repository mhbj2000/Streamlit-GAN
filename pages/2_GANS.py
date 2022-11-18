import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="GANS Demonstration", layout="wide")

with st.container():
    col1, col2, col3,= st.columns(3)
    with col2:
        st.header('Clear to Rain GAN Model')
#potential headers
#st.header('GAN VISUALIZER')
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
    #st.subheader('Clear to Rain Model')
    st.markdown("""
    <style>
    .main-text {
        font-size:26px !important;
        text-align: left;
        line-height: 2.0;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    .subheader {
        font-size:26px !important;
        text-align: center;
        line-height: 2.0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    .headers {
        font-size:32px !important;
        text-align: center;
        line-height: 2.0;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    
    col1,col2,col3 = st.columns(3)
    with col2: #CONTROLS FOR THE ENTIRE ROW
        #st.header('Clear to Rain GAN Model')
        st.markdown('<p class="headers">Controls and Metrics</p>', unsafe_allow_html=True)
        st.markdown('<p class="subheader">Choose an Example</p>', unsafe_allow_html=True)
        model_selector = st.selectbox('Choose an Example',('Example 1', 'Example 2', 'Example 3'),label_visibility="collapsed")
        st.markdown('<p class="subheader">Intermediate Image Number</p>', unsafe_allow_html=True)
        rain_counter = st.slider('Intermediate Image Number', 0,5,label_visibility="collapsed")
        if model_selector == 'Example 1':
            true_counter = rain_counter + 40
            rain_timelapse_picture = Image.open('IntermediatePic/RainFake/Fake4/False_image_'+str(true_counter)+'.png')
            rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse4.mp4', 'rb')
            video_bytes = rain_timelapse.read()
        elif model_selector == 'Example 2':
            true_counter = rain_counter + 160
            rain_timelapse_picture = Image.open('IntermediatePic/RainFake/Fake16/False_image_'+str(true_counter)+'.png')
            rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse16.mp4', 'rb')
            video_bytes = rain_timelapse.read()
        elif model_selector == 'Example 3':
            true_counter = rain_counter + 170
            rain_timelapse_picture = Image.open('IntermediatePic/RainFake/Fake17/False_image_'+str(true_counter)+'.png')
            rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse17.mp4', 'rb')
            video_bytes = rain_timelapse.read()
            
        #st.write('Length of Clear Dataset: 1013 Images  \n',
                 #'Length of Rainy Dataset: 1054 Images  \n',
                 #'Time to Train: 10:30 Hours')
        
        st.markdown('<p class="main-text">Length of Clear Dataset: 1013 Images <br>Length of Rainy Dataset: 1054 <br> Images Time to Train: 10:30 Hours</p>', unsafe_allow_html=True)

    #st.markdown('<p class="big-font"></p>', unsafe_allow_html=True)
 
    with col1:
        st.markdown('<p class="headers">Timelapse</p>', unsafe_allow_html=True)
        st.video(video_bytes)
      
    with col3:
        st.markdown('<p class="headers">Intermediate Images</p>', unsafe_allow_html=True)
        image_resizer = (400,425)
        rain_timelapse_picture = rain_timelapse_picture.resize(image_resizer)
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
