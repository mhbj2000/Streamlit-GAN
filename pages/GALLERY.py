import streamlit as st
from PIL import Image

                   


st.set_page_config(page_title="Gallery", layout="wide")

with st.container():
  st.sidebar.subheader('Controls')
  col1,col2 = st.sidebar.columns(2)
  with col1:
    current_model =st.selectbox('Choose a Model',('Rain','Fog'))
  with col2:
    current_iteration = st.selectbox('Choose an Iteration',(0,1,2,3,4,5,6))
  st.sidebar.write('Iteration 0 is the Real Image and Iteration 5 is the final GAN image.')
  def picGen(current_model,current_iteration):
    current_iteration = current_iteration
    image_list =[]
    
    if current_iteration == 0:
      for i in range(0,20):
        current_image = Image.open('IntermediatePic/Real/Real_image_'+ str(i) + '.png')
        current_image = current_image.resize((500,500))
        image_list.append(current_image)
      return image_list
        
    else:     
      for i in range(0,20):
        current_image = Image.open('IntermediatePic/'+str(current_model)+'Fake/Fake'+ str(i)+'/False_image_'+str(current_iteration)+'.png')
        current_image = current_image.resize((500,500))
        image_list.append(current_image)
        current_iteration = current_iteration + 10
      return image_list
    
  picGen(current_model,current_iteration)

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
picDisplay()

