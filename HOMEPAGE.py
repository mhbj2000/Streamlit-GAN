import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="GANS", layout="wide")

#content of main_page

#header
with open("design.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>WHAT IS A GAN?</h1>", unsafe_allow_html=True)


col1, col2, col3= st.columns(3)
#GENERATOR PARAGRAPH
with col1:
#with st.container():
#container contains old info
    st.markdown('##')

    st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
        text-align: justify;
        text-align-last: left;
        word-spacing:2px

    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">The purpose of the Generator is to generate plausible data. This is with the goal of those plausible instances becoming negative examples for training the Discriminator.</p>', unsafe_allow_html=True)

#DISCRIMINATOR PARAGRAPH 
with col3:
    
    st.markdown('##')

    st.markdown("""
    <style>
    .big-font2 {
        font-size:24px !important;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font2">The Discriminator is meant to identify fake data created by the Generator from real data and issue the Generator a penalty for producing implausible results.</p>', unsafe_allow_html=True)

#HERE IS WHERE GIF GOES
#col1, col2, col3 = st.columns(3)
#with col1:
#    file_ = open("DiscriminatorAnim.gif", "rb")
#    contents = file_.read()
#    data_url = base64.b64encode(contents).decode("utf-8")
#    file_.close()

#    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Gear gif">',unsafe_allow_html=True,)
    
#col2.markdown(video_html, unsafe_allow_html=True)
    

#VIDEO   
with st.container():
    video_file = open('GAN_SYSTEM.mp4', 'rb')
    video_bytes = video_file.read()
    
    st.video(video_bytes)
    

#GAN SYSTEM VIDEO LOOP   
#col1, col2 = st.columns([1, 1])
#with col1:
    
#    video_html = """
#    <video controls width = "250" autoplay="true" muted="true loop="true">
#    <source
#            src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm"
#            type="video/mp4" />
#    </video>
#    """
#    col2.markdown(video_html, unsafe_allow_html=True)
     
#col2.markdown(video_html, unsafe_allow_html=True)

