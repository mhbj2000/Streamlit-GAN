import streamlit as st
from PIL import Image


st.set_page_config(page_title="Gallery", layout="wide")
pic_list = []
def picGen(pictures):
    fileName = "Pic/Test_"
    fileTypeName = ".png"
    newsize = (200, 200)
    picTest_list = []
    for i in range(1,26):
       # st.write(fileName + str(i)+fileTypeName)
        pic_test = Image.open(fileName+str(i)+fileTypeName)
        pic_test = pic_test.resize(newsize)
        picTest_list.append(pic_test)
    return picTest_list
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
 
with st.container():
    #image container
    st.write("---")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    if not picTest_list:
        st.write('')
    else:
        
        nextcol = 1
        newsize = (500,500)
        for i in range(len(picTest_list)):
            picture_result = picTest_list[i].resize(newsize)
            if(nextcol == 6):
                with col6:
                    st.image(picture_result)
                    nextcol = 1
            elif (nextcol == 5):
                with col5:
                    st.image(picture_result)
                    nextcol = 6
            elif (nextcol == 4):
                with col4:
                    st.image(picture_result)
                    nextcol = 5
            elif (nextcol == 3):
                with col3:
                    st.image(picture_result)
                    nextcol = 4
            elif (nextcol == 2):
                with col2:
                    st.image(picture_result)
                    nextcol = 3
            elif (nextcol == 1):
                with col1:
                    st.image(picture_result)
                    nextcol = 2
                   
