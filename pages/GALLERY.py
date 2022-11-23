import streamlit as st
from PIL import Image


#future improvements
#improve the image displaying function           


st.set_page_config(page_title="Gallery", layout="wide")

with st.container():
  #intialize columns in sidebar to place buttons
  st.sidebar.subheader('Controls')
  col1,col2 = st.sidebar.columns(2)
  with col1:
    #display and intialize the model selectbox
    current_model =st.selectbox('Choose a Model',('Rain','Fog'))
  with col2:
    #display and intialize the iteration selectbox
    current_iteration = st.selectbox('Choose an Iteration',(0,1,2,3,4,5,6))
  st.sidebar.write('Iteration 0 is the Real Image and Iteration 6 is the final GAN image.')
  #define function to take images out of folder, resize them, and add them into a empty list
  #takes the data from the widgets as parameters
  def picGen(current_model,current_iteration):
    current_iteration = current_iteration
    #create empty list 
    image_list =[]
    #added this if statement so we can show the original images if the iteration == 0 
    if current_iteration == 0:
      for i in range(0,20):
        #opens image
        current_image = Image.open('IntermediatePic/Real/Real_image_'+ str(i) + '.png')
        #resizes image
        current_image = current_image.resize((500,500))
        #adds image to list
        image_list.append(current_image)
      return image_list
    
    # for any iteration other than 0 it can be ran thru this loop
    else:     
      for i in range(0,20):
        #opens image
        current_image = Image.open('IntermediatePic/'+str(current_model)+'Fake/Fake'+ str(i)+'/False_image_'+str(current_iteration)+'.png')
        #resizes image
        current_image = current_image.resize((500,500))
        #adds image to list
        image_list.append(current_image)
        # we add to the current_iteration variable so we pull the correct image from the folder
        # since every picture has 9 different iterations if we add 10 we can get to the same iteration of the next image
        current_iteration = current_iteration + 10
      return image_list
  
#image container
with st.container():
  #intialize columns
  col1, col2, col3, col4 = st.columns(4)
  def picDisplay():
    # fill up image list
    image_list = picGen(current_model,current_iteration)
    #intialize our starting point for image display
    nextcol = 1
    for i in range(len(image_list)):
      if(nextcol == 4):
        with col4:
          #diplays image in column 4 
          st.image(image_list[i])
          nextcol = 1
      elif (nextcol == 3):
        with col3:
          #diplays image in column 3
          st.image(image_list[i])
          nextcol = 4
      elif (nextcol == 2):
        with col2:
          #diplays image in column 2
          st.image(image_list[i])
          nextcol = 3
      elif (nextcol ==1):
        with col1:
          #diplays image in column 1
          st.image(image_list[i])
          nextcol = 2
picDisplay()

