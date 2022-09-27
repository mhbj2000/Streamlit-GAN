import streamlit as st

st.set_page_config(page_title="GANS", layout="wide")

#content of main_page
def main_page():


    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col3:
            st.title("GANS DEMO ")

    with st.container():
        
        st.write("A generative adversarial network (GAN) is a deep neural network that is trained with existing training data to generate new data of similar characteristics to the training data. For a GAN to work it needs two neural networks the generator, which is trained to produce fake data, and the discriminator, which is trained to distinguish the generator’s fake data from real examples. If the fake data generated is easily recognized as implausible by the discriminator, then the generator is penalized and must try again until it generates something plausible.  ")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "START HERE": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

