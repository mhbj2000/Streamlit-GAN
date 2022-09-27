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
    col1, col2, col3, col4, col5, col6= st.columns(6)
    with col1:
        st.image(img_1)
    with col2:
        st.image(img_0)

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
        with col2:
            st.image("https://static.streamlit.io/examples/dice.jpg")
        
