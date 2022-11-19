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
    

with st.container():
    col1, col2, col3,= st.columns(3)
    with col2:
        st.header('GAN MODEL VISUALIZER')


tab1,tab2,tab3 =st.tabs(['Clear To Rain Model Visualizer', 'Clear to Fog Model','testing'])
# ---- GAN Rain Visualizer | Row 1 ----         
with tab1:
    image_resizer = (400,425)
    col1,col2,col3 = st.columns(3)
    with col2:
        st.subheader('Image Slider')
        #st.markdown('<p class="main-text">Length of Clear Dataset: 1013 Images <br>Length of Rainy Dataset: 1054 Images <br> Time to Train Rain Model: 10:30 Hours</p>', unsafe_allow_html=True)
        #st.write('The total length of the clear image dataset = 1013 images  \n')
        #st.write('The total length of the rainy image dataset = 1054 images  \n')
        #st.write('The total time to train the clear to rainy model was: 10:30hours')
        
        image_counter = st.slider('Sample Image Display Slider',1,5,1,key = 'clear_image slider',label_visibility ='visible')
        clear_or_rainy = st.selectbox('Choose an option',('Clear Image Dataset','Rainy Image Dataset'))
        for i in range(12):
            st.markdown('#')
 
    with col1:
        #st.subheader('Sample of Clear Image Dataset')
        if clear_or_rainy == 'Clear Image Dataset':
            clear_image = Image.open('IntermediatePic/Clear Images/Clear_image_'+str(image_counter)+'.png')
            clear_image = clear_image.resize(image_resizer)
            st.image(clear_image,'Provided by CityScape')
        elif clear_or_rainy == 'Rainy Image Dataset':
            rainy_image = Image.open('IntermediatePic/Rainy Images/rainy_image_'+str(image_counter)+'.png')
            rainy_image = rainy_image.resize(image_resizer)
            st.image(rainy_image,'Provided by CityScape') 
            
            
            
                                      
        #st.subheader('Clear Image Dataset: 1013 Images')
        #clear_image = Image.open('IntermediatePic/Clear Images/Clear_image_'+str(image_counter)+'.png')
        #clear_image = clear_image.resize(image_resizer)
        #st.image(clear_image,'Provided by CityScape')
    with col3:
        #st.markdown('<p class="main-text">Length of Clear Dataset: 1013 Images <br>Length of Rainy Dataset: 1054 Images <br> Time to Train Rain Model: 10:30 Hours</p>', unsafe_allow_html=True)
        #for i in range(12):
            #st.markdown('#')
        #st.subheader('Sample of Rainy Image Dataset')
        #st.subheader('Rainy Image Dataset: 1054 Images')
        rainy_image = Image.open('IntermediatePic/Rainy Images/rainy_image_'+str(image_counter)+'.png')
        rainy_image = rainy_image.resize(image_resizer)
        st.image(rainy_image,'Provided by CityScape')  
with tab2:
    col1,col2,col3 = st.columns(3)
    with col2: #CONTROLS FOR THE MODEL
        #st.markdown('<p class="headers">Controls and Metrics</p>', unsafe_allow_html=True)
        st.markdown('<p class="subheader">Choose an Example</p>', unsafe_allow_html=True)
        model_selector = st.selectbox('Choose an Example',('Example 1', 'Example 2', 'Example 3'),label_visibility='collapsed')
        st.markdown('<p class="subheader">Intermediate Image Number</p>', unsafe_allow_html=True)
        rain_counter = st.slider('Intermediate Image Number', 0,6,label_visibility="collapsed")            
        if model_selector == 'Example 1':
            if rain_counter == 0:
                st.write(rain_counter)
                rain_timelapse_picture = Image.open('IntermediatePic/Real/Real_image_4.png')
            else:
                true_counter = rain_counter + 39
                rain_timelapse_picture = Image.open('IntermediatePic/RainFake/Fake4/False_image_'+str(true_counter)+'.png')
            rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse4.mp4', 'rb')
            video_bytes = rain_timelapse.read()
        elif model_selector == 'Example 2':
            if rain_counter == 0:
                rain_timelapse_picture = Image.open('IntermediatePic/Real/Real_image_16.png')
                pass
            else:
                true_counter = rain_counter + 159
                rain_timelapse_picture = Image.open('IntermediatePic/RainFake/Fake16/False_image_'+str(true_counter)+'.png')
            rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse16.mp4', 'rb')
            video_bytes = rain_timelapse.read()
        elif model_selector == 'Example 3':
            if rain_counter == 0:
                rain_timelapse_picture = Image.open('IntermediatePic/Real/Real_image_17.png')
                pass
            else:
                true_counter = rain_counter + 169
                rain_timelapse_picture = Image.open('IntermediatePic/RainFake/Fake17/False_image_'+str(true_counter)+'.png')
            rain_timelapse = open('Time-lapse/RainTimelapse/Timelapse17.mp4', 'rb')
            video_bytes = rain_timelapse.read()
            
        st.markdown('<p class="main-text">Length of Clear Dataset: 1013 Images <br>Length of Rainy Dataset: 1054 Images <br> Time to Train Rain Model: 10:30 Hours</p>', unsafe_allow_html=True)
 
    with col1:
        st.markdown('<p class="headers">Timelapse</p>', unsafe_allow_html=True)
        st.video(video_bytes)
      
    with col3:
        st.markdown('<p class="headers">Intermediate Images</p>', unsafe_allow_html=True)
        #image_resizer = (400,425)
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
        st.markdown('<p class="main-text">Length of Clear Dataset: 1013 Images <br>Length of Fog Dataset: 1008 Images <br> Time to Train Fog Model: 10:30 Hours</p>', unsafe_allow_html=True)
        
    with col1:
        st.markdown('<p class="headers">Timelapse</p>', unsafe_allow_html=True)
        st.video(video_bytes)
    with col3:
        st.markdown('<p class="headers">Intermediate Images</p>', unsafe_allow_html=True)
        image_resizer = (400,425)
        fog_timelapse_picture = fog_timelapse_picture.resize(image_resizer)
        st.image(fog_timelapse_picture)        
        
