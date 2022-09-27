import streamlit as st
from PIL import Image

                   


st.set_page_config(page_title="Gallery", layout="wide")
pic_list = []
with st.container():
    #image container
    st.write("---")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    def picDisplay(picResult):
        
        nextcol = 1
        newsize = (500,500)
        for i in range(len(picResult)):
            picture_result = picResult[i].resize(newsize)
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
        return 0
                   

def picGen(pictures):
    fileName = "Pic/Test_"
    fileTypeName = ".png"
    newsize = (200, 200)
    picTest_list = []
    for i in range(1,25):
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
        if st.sidebar.button("Start Gallery"):
            picResult = picGen(GANData)
            picDisplay(picResult)
        #st.sidebar.button("Randomize Synthetic Data") 
    #with right_column:
        #if st.sidebar.button("Clear Input"):
            #picResult = []
        #st.sidebar.button("Stop")
 

