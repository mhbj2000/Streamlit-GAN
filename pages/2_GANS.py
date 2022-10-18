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
        imgTest= imgTest.resize(newsize)
        picTest.append(imgTest)
    return picTest

st.set_page_config(page_title="GANS Demonstration", layout="wide")


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
        
with st.container():
    #Real Images being displayed
    real_image_1 = Image.open('Pic/01.jpg')
    real_image_2 = Image.open('Pic/02.jpg')
    real_image_3 = Image.open('Pic/03.jpg')
    new_size = (200,200)
    real_image_1.resize(new_size)
    real_image_2.resize(new_size)
    real_image_3.resize(new_size)
    st.write('---')
    st.header('Example of Real Images')
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image(real_image_1)
    with col2:
        st.image(real_image_2)
    with col3:
        st.image(real_image_3)
        
with st.container():
    st.write('---')
    st.header('Example of Synthetic Images')
    col1,col2,col3 = st.columns(3)
    # Synthetic Images being displayed
    fake_image_1 = 
    fake_image_2 = 
    fake_image_3 = 
    new_size=(200,200)
    fake_image_1.resize(new_size)
    fake_image_2.resize(new_size)
    fake_image_3.resize(new_size)
        
            

with st.container():
    #image container
    st.write("---")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    if not picResult:
        st.write("")
    else:
        nextcol = 1
        newsize = (500, 500)
        for i in range(len(picResult)):
            imgRe= picResult[i].resize(newsize)
            if (nextcol == 6):
                with col6:
                    st.image(imgRe,caption="Test_"+str(i))
                    nextcol = 1
            elif (nextcol == 5):
                with col5:
                    st.image(imgRe,caption="Test_"+str(i))
                    nextcol = 6
            elif (nextcol == 4):
                with col4:
                    st.image(imgRe,caption="Test_"+str(i))
                    nextcol = 5
            elif (nextcol == 3):
                with col3:
                    st.image(imgRe,caption="Test_"+str(i))
                    nextcol = 4
            elif (nextcol == 2):
                with col2:
                    st.image(imgRe,caption="Test_"+str(i))
                    nextcol = 3
            elif (nextcol == 1):
                with col1:
                    st.image(imgRe,caption="Test_"+str(i))
                    nextcol = 2

with st.container():
    with st.expander("Metrics and Results"):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Metrics")
            st.write(seedData , "real images")
            st.write(synData ,"synthetic images")
            GANData = seedData*synData
            st.write(GANData,"GAN images")
            st.write("Generated in - minutes and - seconds")
