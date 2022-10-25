import streamlit as st
import base64

st.set_page_config(page_title="GANS", layout="wide")

#content of main_page

#header
with open("design.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>HOW IT WORKS</h1>", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
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
    with col2:
        file_ = open("Gear_Turn.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Gear gif">',unsafe_allow_html=True,)


with st.container():
    
    st.markdown('##')

    st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">The purpose of the discriminator is to identify real data from fake data created by our generator. The data that the discriminator identifies as false information is sent back to the generator for it to improve upon.</p>', unsafe_allow_html=True)
        
with st.container():
    file_ = open("DiscriminatorAnim.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Gear gif">',unsafe_allow_html=True,)
        
with st.container():
    
    st.markdown('##')

    st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">The purpose of our generator is to create fake data, taking feedback from the discriminator and applying it to make more realistic fake images and make the discriminator think the fake images are real. </p>', unsafe_allow_html=True)
        
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.image("./wip_photo.png")
