import streamlit as st
from PIL import Image

                   


st.set_page_config(page_title="Gallery", layout="wide")

with st.container():
  st.sidebar.subheader('Controls')
  col1,col2 = st.sidebar.columns(2)
  with col1:
    current_model =st.selectbox('Choose a Model',('Rain','Fog'))
  with col2:
    current_iteration = st.selectbox('Choose an Iteration',(0,1,2,3,4,5))
  def picGen(current_model,current_iteration):
    current_iteration = current_iteration
    image_list =[]
    #image_string = ('IntermediatePic/'+(current_model)+'Fake/Fake'+(fake_counter)+ 'False_image_'+str(current_iteration)+'.png')
    for i in range(0,20):
      current_image = Image.open('IntermediatePic/'+str(current_model)+'Fake/Fake'+(str(i))+'/False_image_'+str(current_iteration)+'.png')
      current_image = current_image.resize((200,200))
      image_list.append(current_image)
      current_iteration = current_iteration + 10
    return image_list
  picGen(current_model,current_iteration)
  #picDisplay()
with st.container():
  col1, col2, col3, col4 = st.columns(4)
    def picDisplay():
      image_list = picGen(current_model,current_iteration)
      nextcol = 1
      for i in range(len(image_list)):
        if(nextcol == 4):
          with col4:
            st.image(image_list[i])
            nextcol = 1
        elif (nextcol == 3):
          with col3:
            st.image(image_list[i])
            nextcol = 4
        elif (nextcol == 2):
          with col2:
            st.image(image_list[i])
            nextcol = 3
        elif (nextcol ==1):
          with col1:
            st.image(image_list[i])
            nextcol = 2
        return 0
  picDisplay()
  
    
    
 
                                
  
    






if 'start_index' not in st.session_state:
    st.session_state.start_index = 1
pic_list = []
#st.session_state.start_index = 1
#start_index = 1
with st.container():
    #image container
    st.write("---")
    col1, col2, col3, col4 = st.columns(4)
    def picDisplay():
      image_list = picGen(current_model,current_iteration)
      nextcol = 1
      for i in range(len(image_list)):
        if(nextcol == 4):
          with col4:
            st.image(image_list[i])
            nextcol = 1
        elif (nextcol == 3):
          with col3:
            st.image(image_list[i])
            nextcol = 4
        elif (nextcol == 2):
          with col2:
            st.image(image_list[i])
            nextcol = 3
        elif (nextcol ==1):
          with col1:
            st.image(image_list[i])
            nextcol = 2
        return 0

        
        
        #nextcol = 1
        #newsize = (500,500)
        #for i in range(len(picResult)):
            #picture_result = picResult[i].resize(newsize)
            #if(nextcol == 6):
                #with col6:
                    #st.image(picture_result)
                    #nextcol = 1
            #elif (nextcol == 5):
                #with col5:
                    #st.image(picture_result)
                    #nextcol = 6
            #elif (nextcol == 4):
                #with col4:
                    #st.image(picture_result)
                    #nextcol = 5
            #elif (nextcol == 3):
                #with col3:
                    #st.image(picture_result)
                    #nextcol = 4
            #elif (nextcol == 2):
                #with col2:
                    #st.image(picture_result)
                    #nextcol = 3
            #elif (nextcol == 1):
                #with col1:
                    #st.image(picture_result)
                    #nextcol = 2
        #return 0
                   

def picGen(current_model,current_iteration):
  image_list =[]
  image_string = ('IntermediatePic/'+(current_model)+'Fake/Fake'+(fake_counter)+ 'False_image_'+str(current_iteration)+'.png')
  for i in range(0,20):
    current_image = Image.open('IntermediatePic/'+(current_model)+'Fake/Fake'+(i)+ 'False_image_'+str(current_iteration)+'.png')
    current_image = current_image.resize((200,200))
    image_list.append(current_image)
  return image_list 
                 
    #st.write(start_index)
    #fileName = "Pic/Test_"
    #fileTypeName = ".png"
    #newsize = (200, 200)
    #picTest_list = []
    #for i in range(start_index,start_index+12):
        #pic_test = Image.open(fileName+str(i)+fileTypeName)
        #pic_test = pic_test.resize(newsize)
        #picTest_list.append(pic_test)
    #return picTest_list
#with st.container():
    #st.sidebar.subheader("CONTROLS")
    #left_column, right_column = st.sidebar.columns(2)
    #with right_column:
      #st.slider('deez',0,5,0)
    #with left_column:
        #weather_options = ['Rain','Snow','Sunny','Overcast','Night','Cloudy']
        #weather = st.select_slider("Choose a Type of Weather",options = weather_options)
        #st.write('The current weather is:',weather)
        #if st.sidebar.button("Start Gallery"):
            #picResult = picGen(1)
            #picDisplay(picResult)
        #if st.sidebar.button("Next Page") :
          #st.session_state.start_index += 12
          #start_index += 12
          #st.write(st.session_state.start_index)
          #picResult = []
          #picResult = picGen(st.session_state.start_index)
          #picDisplay(picResult)
        #if st.sidebar.button('Previous Page') :
          #st.session_state.start_index -=12
          #start_index = start_index - 12
          #st.write(st.session_state.start_index)
          #picResult = []
          #picResult = picGen(st.session_state.start_index)
          #picDisplay(picResult)
 

