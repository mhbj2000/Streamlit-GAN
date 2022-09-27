import streamlit as st
from PIL import Image


st.set_page_config(page_title="Gallery", layout="wide")
pic_list = []
def picGen(pictures):
    fileName = "Pic/Test_"
    fileTypeName = ".png"
    newsize = (200, 200)
    picTest = []
    for i in range(26):
      picture = Image.open(filename+str(i+fileTypeName))
      picture = picture.resize(newsize)
      picTest.append(picture)
    return picTest
with st.container():
    st.sidebar.subheader("CONTROLS")
    #st.slider("Slider tester", 1, 5000, 2000)
    seedData = st.sidebar.slider("Seed Data",1,5,5)
    synData = st.sidebar.slider("Synthetic Data",1,5,5)
    GANData = seedData*synData
    left_column, right_column = st.sidebar.columns(2)
    with left_column:
        if st.sidebar.button("Generate GANs"):
            picResult = picGen(GANData)
        st.sidebar.button("Randomize Synthetic Data") 
    with right_column:
        if st.sidebar.button("Clear Input"):
            picResult = []
        st.sidebar.button("Stop")
                           
