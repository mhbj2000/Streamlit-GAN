import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="GANS Demonstration", layout="wide")
with st.container():
    #HTML FONT BUILDER
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
    .widget_font {
        font-size:26px !important;
        text-align: center;
        line-height: 2.0;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    
    
    st.markdown("""
    <style>
    .image-caption-text {
        font-size:26px !important;
        text-align: center;
        line-height: 2.0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    
    st.markdown("""
    <style>
    .main-subtext {
        font-size:20px !important;
        text-align: left;
        line-height: 2.0;
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
    }
    </style>
    """, unsafe_allow_html=True)
    


tab1,tab2,tab3 =st.tabs(['GAN Model Training','Clear To Rainy Model Visualizer', 'Clear to Foggy Model Visualizer',])
# ---- GAN Model Trainer Tab ----         
with tab1:
    #intialize image resizer
    image_resizer = (700,425)
    #intialize columns for layout
    col1,col2 = st.columns(2)
    with col2: 
        #Displays all the Metrics and also intializes the slider
        st.markdown('<p class="widget_font">Image Display Slider</p>', unsafe_allow_html=True)
        image_counter = st.slider('Example Image Display Slider',1,5,1,key = 'clear_image slider',label_visibility ='collapsed')
        st.markdown('<p class="main-text">Clear to Rain Model</p>', unsafe_allow_html=True)
        st.markdown('<p class="main-subtext">Trained using the Clear and Rainy Dataset.</p>', unsafe_allow_html=True)
        st.markdown('<p class="main-subtext">Time to Train: 10.5 hrs approx.</p>', unsafe_allow_html=True)
        st.write('---')
        st.markdown('<p class="main-text">Clear to Fog Model</p>', unsafe_allow_html=True)
        st.markdown('<p class="main-subtext">Trained using the Clear and Foggy Dataset.</p>', unsafe_allow_html=True)
        st.markdown('<p class="main-subtext">Time to Train: 10.5 hrs approx.</p>', unsafe_allow_html=True)

    with col1:
        #Displays set of images based on the selectbox and slider variables
        st.markdown('<p class="widget_font">Choose a Dataset</p>', unsafe_allow_html=True)
        #intialized selectbox
        clear_or_rainy = st.selectbox('Choose a Dataset',('Clear Image Dataset','Rainy Image Dataset','Foggy Image Dataset'),label_visibility = 'collapsed')
        if clear_or_rainy == 'Clear Image Dataset':
            clear_image = Image.open('IntermediatePic/Clear Images/Clear_image_'+str(image_counter)+'.png')
            clear_image = clear_image.resize(image_resizer)
            st.image(clear_image,'Provided by CityScapes')
            st.markdown('<p class="image-caption-text">Total Length of Clear Dataset: 1013 Images</p>', unsafe_allow_html=True)
        elif clear_or_rainy == 'Rainy Image Dataset':
            rainy_image = Image.open('IntermediatePic/Rainy Images/rainy_image_'+str(image_counter)+'.png')
            rainy_image = rainy_image.resize(image_resizer)
            st.image(rainy_image,'Provided by CityScapes')
            st.markdown('<p class="image-caption-text">Total Length of Rainy Dataset: 1054 Images</p>', unsafe_allow_html=True)
        elif clear_or_rainy == 'Foggy Image Dataset':
            foggy_image = Image.open('IntermediatePic/Foggy Images/foggy_image_'+str(image_counter)+'.png')
            foggy_image = foggy_image.resize(image_resizer)
            st.image(foggy_image,'Provided by CityScapes')
            st.markdown('<p class="image-caption-text">Total Length of Foggy Dataset: 1008 Images</p>', unsafe_allow_html=True)
             
        
#--- Clear to Rainy Model Tab  
with tab2:
    col1,col2 = st.columns(2)
    with col2:
        st.markdown('<p class="subheader">Choose an Example</p>', unsafe_allow_html=True)
        #---Sets selectbox = to one of 3 strings---
        model_selector = st.selectbox('Choose an Example',('Example 1', 'Example 2', 'Example 3'),label_visibility='collapsed')
        st.markdown('<p class="subheader">Image Iterations</p>', unsafe_allow_html=True)
        #--- Sets rain_counter to a number 0-6---
        rain_counter = st.slider('Intermediate Image Number', 0,6,label_visibility="collapsed")
        
    with col1:
        if model_selector == 'Example 1':
            if rain_counter == 0:
                #---opens the original image before it was ran through the GAN---
                rain_timelapse_picture = Image.open('IntermediatePic/Real/Real_image_4.png')
            else:
                #--- adds to the counter so it can pull the correct photo from the folder---
                true_counter = rain_counter + 39
                rain_timelapse_picture = Image.open('IntermediatePic/RainFake/Fake4/False_image_'+str(true_counter)+'.png')
            rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse4.mp4', 'rb')
            video_bytes = rain_timelapse.read()
        elif model_selector == 'Example 2':
            #---opens the original image before it was ran through the GAN---
            if rain_counter == 0:
                rain_timelapse_picture = Image.open('IntermediatePic/Real/Real_image_16.png')
            else:
                #--- adds to the counter so it can pull the correct photo from the folder---
                true_counter = rain_counter + 159
                rain_timelapse_picture = Image.open('IntermediatePic/RainFake/Fake16/False_image_'+str(true_counter)+'.png')
            rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse16.mp4', 'rb')
            video_bytes = rain_timelapse.read()
        elif model_selector == 'Example 3':
            if rain_counter == 0:
                #---opens the original image before it was ran through the GAN---
                rain_timelapse_picture = Image.open('IntermediatePic/Real/Real_image_17.png')
            else:
                #--- adds to the counter so it can pull the correct photo from the folder---
                true_counter = rain_counter + 169
                rain_timelapse_picture = Image.open('IntermediatePic/RainFake/Fake17/False_image_'+str(true_counter)+'.png')
            rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse17.mp4', 'rb')
            video_bytes = rain_timelapse.read()
            
    with col1:
        #---Displays Video---
        st.video(video_bytes)
      
    with col2:
        #---Resizes Image---
        image_resizer = (400,400)
        rain_timelapse_picture = rain_timelapse_picture.resize(image_resizer)
        #---Displays Image---
        st.image(rain_timelapse_picture)
        
# ---- Clear to Fog Model tab ----       
with tab3:
    col1,col2 = st.columns(2)
    with col2: #CONTROLS FOR THE MODEL
        st.markdown('<p class="subheader">Choose an Example</p>', unsafe_allow_html=True)
        model_selector = st.selectbox('Choose an Example',('Example 1', 'Example 2', 'Example 3'), key = '2nd selectbox',label_visibility="collapsed")
        st.markdown('<p class="subheader">Image Iterations</p>', unsafe_allow_html=True)
        fog_counter = st.slider('Intermediate Image Number', 0,6, key = '2nd slider',label_visibility="collapsed")
        if model_selector == 'Example 1':
            if fog_counter == 0:
                fog_timelapse_picture = Image.open('IntermediatePic/Real/Real_image_4.png')
            else:
                true_counter = fog_counter + 39
                fog_timelapse_picture = Image.open('IntermediatePic/FogFake/Fake4/False_image_'+str(true_counter)+'.png')
            fog_timelapse = open('Time-lapse/FogTimelapse/Timelapse4.mp4', 'rb')
            video_bytes = fog_timelapse.read()
        elif model_selector == 'Example 2':
            if fog_counter == 0:
                fog_timelapse_picture = Image.open('IntermediatePic/Real/Real_image_16.png')
            else:
                true_counter = fog_counter + 159
                fog_timelapse_picture = Image.open('IntermediatePic/FogFake/Fake16/False_image_'+str(true_counter)+'.png')
            fog_timelapse = open('Time-lapse/FogTimelapse/Timelapse16.mp4', 'rb')
            video_bytes = fog_timelapse.read()
        elif model_selector == 'Example 3':
            if fog_counter == 0:
                fog_timelapse_picture = Image.open('IntermediatePic/Real/Real_image_17.png')
            else:    
                true_counter = fog_counter + 169
                fog_timelapse_picture = Image.open('IntermediatePic/FogFake/Fake17/False_image_'+str(true_counter)+'.png')
            fog_timelapse = open('Time-lapse/FogTimelapse/Timelapse17.mp4', 'rb')
            video_bytes = fog_timelapse.read()        
    with col1:
        #---Display video and label it---
        st.markdown('<p class="headers">Timelapse</p>', unsafe_allow_html=True)
        st.video(video_bytes)
    with col2:
        #---Display image, resize, and label---
        #st.markdown('<p class="headers">Intermediate Images</p>', unsafe_allow_html=True)
        image_resizer = (400,400)
        fog_timelapse_picture = fog_timelapse_picture.resize(image_resizer)
        st.image(fog_timelapse_picture)        
        
