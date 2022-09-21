import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title="GANS Demonstration", layout="wide")

img_0 = Image.open("discriminator.PNG")
img_1 = Image.open("generator.PNG")


with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.subheader("Options")
    with col3:
        st.subheader("Generator")
    with col4:
        st.subheader("Discriminator")
    with col5:
        st.subheader("Output")

# ---- SIDE SLIDER ---- 
with st.container():
    st.write("---")
    #st.slider("Slider tester", 1, 5000, 2000)
    seedData = st.sidebar.slider("Seed Data",1,5,5)
    synData = st.sidebar.slider("Synthetic Data",1,5,5)
    left_column, right_column = st.sidebar.columns(2)
    with left_column:
        st.sidebar.button("Generate GANs")
        st.sidebar.button("Randomize Synthetic Data")
    with right_column:
        st.sidebar.button("Clear Input")
        st.sidebar.button("Stop")
    st.write("---")
    st.subheader("Metrics")
    st.write(seedData , "real images")
    st.write(synData ,"synthetic images")
    GANData = seedData*synData
    st.write(GANData,"GAN images")
    st.write("Generated in - minutes and - seconds")        
        
with st.container():
    col1, col2, col3, col4, col5, col6= st.columns(6)
    with col1:
        st.button('Randomize Synthetic Data')
        st.button('Run Generator')
    with col2:
        st.button('Clear Input')
        st.button('Stop')
    with col3:
        st.image(img_1)
    with col4:
        st.image(img_0)

with st.container():
    st.subheader("---")

with st.container():
    with st.expander("Metrics and Results"):
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://static.streamlit.io/examples/dice.jpg")
            
        with col2:
            st.subheader("Metrics")
            st.write("10 real images")
            st.write("4000 synthetic images")
            st.write("8000 GAN images")
            st.write("Generated in 1 minute and 30 seconds")
        
