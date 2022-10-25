import streamlit as st
import base64

st.set_page_config(page_title="GANS", layout="wide")

#content of main_page

#header
with open("design.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>WHAT IS A GAN?</h1>", unsafe_allow_html=True)

with st.container():

    st.markdown('##')

    st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">A generative adversarial network (GAN) is a deep neural network that is trained with existing training data to generate new data of similar characteristics to the training data. For a GAN to work it needs two neural networks the generator, which is trained to produce fake data, and the discriminator, which is trained to distinguish the generator’s fake data from real examples. If the fake data generated is easily recognized as implausible by the discriminator, then the generator is penalized and must try again until it generates something plausible.  </p>', unsafe_allow_html=True)

#HERE IS WHERE GIF GOES
col1, col2, col3 = st.columns(3)
with col1:
    file_ = open("DiscriminatorAnim.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Gear gif">',unsafe_allow_html=True,)

with st.container():
    image = Image.open('GAN SYSTEM.PNG')
    st.image(image, caption ='Final Animation Demo'
