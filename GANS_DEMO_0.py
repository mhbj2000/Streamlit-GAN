import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import random

picResult = []

def rando(gStop):
    fileName = "Pic/Test_"
    fileTypeName = ".png"
    newsize = (200, 200)
    picTest = []
    k = random.sample(range(1,31), gStop)
    for i in range(1,gStop):
        imgTest = Image.open(fileName+str(k[i])+fileTypeName)
        #imgTest= imgTest.resize(newsize)
        picTest.append(imgTest)
    return picTest

st.set_page_config(page_title="GANS Demonstration", layout="wide")

img_0 = Image.open("discriminator.PNG")
img_1 = Image.open("generator.PNG")


with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
#potential headers

# ---- SIDE BAR COTNROLS ---- 
with st.container():
    st.sidebar.subheader("CONTROLS")
    #st.slider("Slider tester", 1, 5000, 2000)
    seedData = st.sidebar.slider("Seed Data",1,5,5)
    synData = st.sidebar.slider("Synthetic Data",1,5,5)
    GANData = seedData*synData
    left_column, right_column = st.sidebar.columns(2)
    with left_column:
        if st.sidebar.button("Generate GANs"):
            picResult = rando(GANData)
        st.sidebar.button("Randomize Synthetic Data") 
    with right_column:
        if st.sidebar.button("Clear Input"):
            picResult = []
        st.sidebar.button("Stop")
    with st.expander("Metrics and Results"):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Metrics")
            st.write(seedData , "real images")
            st.write(synData ,"synthetic images")
            GANData = seedData*synData
            st.write(GANData,"GAN images")
            st.write("Generated in - minutes and - seconds")
        with col2:
            st.image("https://static.streamlit.io/examples/dice.jpg")
            
with st.container():
    col1, col2, col3, col4, col5, col6= st.columns(6)
    with col1:
        st.image(img_1)
    with col2:
        st.image(img_0)

with st.container():
    #image container
    st.subheader("---")
    st.write("---")
    if not picResult:
        st.write("no pic")
    else:
        st.image(picResult, width = 200)


        
