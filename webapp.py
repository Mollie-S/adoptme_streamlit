import streamlit as st
import base64
from PIL import Image

st.set_page_config(page_title="Blueberry", page_icon=":smiley_cat:", initial_sidebar_state="auto")
adopt_title = """
             <h1 style = "color: 332E34; text-align: center" > Blueberry River </h1>
             <h4 style = "color: #2F2523; text-align: center" > Do you want to adopt me? </h4>
             """
st.markdown(adopt_title, unsafe_allow_html=True)
st.sidebar.header("Description")
description = "I'm the most undemanding, calm, and loving cat you've ever seen.\
 Having a sweet personality, I'm also intelligent, inquisitive and playful \
  so you'll never be bored."
contact_info = "Contact my shelter [here](https://www.doamsterdam.nl/contact/)."
address = "Dierenopvang Amsterdam, Ookmeerweg 271 \
1067 SP Amsterdam"
with st.sidebar.container():
    st.write(description)
    st.write(contact_info)
    st.write("Or come and visit me:")
    st.write(address)
main_bg = "./images/philipp-deus-uO95dylxdUM-unsplash.png"
main_bg_ext = "png"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover
    }}
   .sidebar .sidebar-content {{
        # background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-color: black;
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)

img = Image.open("./images/photo-1478098711619-5ab0b478d6e6.jpeg")
st.image(img)
