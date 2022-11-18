import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="GANS Demonstration", layout="wide")

with st.container():
    col1, col2, col3,= st.columns(3)
    with col2:
        st.header('Clear to Rain GAN Model')


tab1,tab2 =st.tabs(['Clear To Rain Model', 'Clear to Fog Model'])
# ---- GAN Rain Visualizer | Row 1 ----         
with tab1:
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
    with col2: #CONTROLS FOR THE MODEL
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
        
        st.markdown('<p class="main-text">Length of Clear Dataset: 1013 Images <br>Length of Rainy Dataset: 1054 Images <br> Images Time to Train: 10:30 Hours</p>', unsafe_allow_html=True)

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
with tab2:
    col1,col2,col3 = st.columns(3)
    with col2: #CONTROLS FOR THE MODEL
        st.markdown('<p class="headers">Controls and Metrics</p>', unsafe_allow_html=True)
        st.markdown('<p class="subheader">Choose an Example</p>', unsafe_allow_html=True)
        model_selector = st.selectbox('Choose an Example',('Example 1', 'Example 2', 'Example 3'), key = '2nd selectbox',label_visibility="collapsed")
        st.markdown('<p class="subheader">Intermediate Image Number</p>', unsafe_allow_html=True)
        fog_counter = st.slider('Intermediate Image Number', 0,5, key = '2nd slider',label_visibility="collapsed")
        if model_selector == 'Example 1':
            true_counter = fog_counter + 40
            fog_timelapse_picture = Image.open('IntermediatePic/FogFake/Fake4/False_image_'+str(true_counter)+'.png')
            fog_timelapse = open('Time-lapse/FogTimelapse/Timelapse4.mp4', 'rb')
            video_bytes = fog_timelapse.read()
        elif model_selector == 'Example 2':
            true_counter = fog_counter + 160
            fog_timelapse_picture = Image.open('IntermediatePic/FogFake/Fake16/False_image_'+str(true_counter)+'.png')
            fog_timelapse = open('Time-lapse/FogTimelapse/Timelapse16.mp4', 'rb')
            video_bytes = fog_timelapse.read()
        elif model_selector == 'Example 3':
            true_counter = fog_counter + 170
            fog_timelapse_picture = Image.open('IntermediatePic/FogFake/Fake17/False_image_'+str(true_counter)+'.png')
            fog_timelapse = open('Time-lapse/FogTimelapse/Timelapse17.mp4', 'rb')
            video_bytes = fog_timelapse.read()
        st.markdown('<p class="main-text">Length of Clear Dataset: 1013 Images <br>Length of Fog Dataset: 1008 Images <br> Images Time to Train: 10:30 Hours</p>', unsafe_allow_html=True)
        
    with col1:
        st.markdown('<p class="headers">Timelapse</p>', unsafe_allow_html=True)
        st.video(video_bytes)
    with col3:
        st.markdown('<p class="headers">Intermediate Images</p>', unsafe_allow_html=True)
        image_resizer = (400,425)
        fog_timelapse_picture = fog_timelapse_picture.resize(image_resizer)
        st.image(fog_timelapse_picture)        
        
