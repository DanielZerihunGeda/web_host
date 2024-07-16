import streamlit as st
import base64
from PIL import Image
from datetime import datetime, timedelta
import pandas as pd
from scr.append import * 
# ---- Setting up the tab ----
dizzys_trumpet = Image.open("images/Dizzys_trumpet.jpg")
st.set_page_config(page_title="DTraning", page_icon=None, layout="centered")

# ---- Using CSS ----
with open("style/style2.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
    Returns
    -------
    The background.
    '''
    main_bg_ext = "jpg"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{get_base64_of_bin_file(main_bg)}) no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_hack("images/milesdavis2.jpg")

# ---- Header ----
title = st.markdown("<h1 style='text-align: center; font-size: 50px;'>DEBO Academy </h1>", unsafe_allow_html=True)
# ---- Registration Form ----
st.markdown('<div class="registration-form">', unsafe_allow_html=True)
st.markdown('<h3>Register Here</h3>', unsafe_allow_html=True)

with st.form(key='registration_form'):
    name = st.text_input("Full Name")
    grade = st.selectbox("Select Grade", ["7th", "8th", "9th", "10th", "11th", "12th"])
    sex = st.selectbox("Sex", ["Male", "Female"])
    phone_number = st.text_input("Phone Number")
    submit_button = st.form_submit_button(label='Join The Waitlist !')

    if submit_button:
            try:
                if name == '' and grade == '' and sex == '' and phone_number == '':
                    st.warning("Please insert all information.")
                else:
                    current_time = datetime.now()
                    data = {
                        'name': [name],
                        'Grade': [grade],
                        'sex': [sex],
                        'Contact': [phone_number],
                        'Timestamp': [current_time.strftime("%Y-%m-%d")]
                    }
                    df = pd.DataFrame(data)
                    append_df_to_gsheet('Trainee', 'Sheet1', df)
                    st.success("We Have Recieved Your Application !!")
            except Exception as e:
                st.error(f'Failed To Accept Your Request Please Contact Administrator !!')
                st.stop()
# ---- Social Media Links ----
st.markdown("""
    <div class="social">
        <div><i class="fab fa-telegram"></i> Telegram</div>
        <div><i class="fab fa-tiktok"></i> TikTok</div>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
