import streamlit as st
from auth.auth_db import register_user, login_user
import os


def auth_page():

    st.markdown("""
    <style>

    /* PROFESSIONAL FONT */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;700;800&display=swap');

    html, body, [class*="css"]{
        font-family:'Inter', sans-serif;
    }

    /* TITLE */

    .title{
        text-align:center;
        font-size:84px !important;
        font-weight:800 !important;
        color:#38bdf8 !important;
        margin-top:10px;
        margin-bottom:20px;
        letter-spacing:1px;
    }

    /* CENTER LOGO */

    .logo-container{
        display:flex;
        justify-content:center;
        align-items:center;
        width:100%;
        text-align:center;
        margin-bottom:5px;
    }

    /* GLASS LOGIN CARD */

    form{
        background:rgba(0,0,0,0.55);
        padding:30px;
        border-radius:14px;
        border:2px solid white !important;
        backdrop-filter: blur(8px);
    }

    /* LABELS */

    label{
        color:white !important;
        font-weight:600;
    }

    /* RADIO BUTTON TEXT */

    div[role="radiogroup"] label p{
        color:white !important;
        font-weight:600 !important;
    }

    div[role="radiogroup"] label span{
        color:white !important;
    }

    /* INPUT BOX */

    div[data-baseweb="input"]{
        background:white !important;
        border:2px solid #38bdf8 !important;
        border-radius:10px;
    }

    div[data-baseweb="input"] input{
        color:black !important;
        background:white !important;
    }

    /* BUTTON */

    .stButton button{
        height:48px;
        width:100%;
        font-size:17px;
        border-radius:10px;
        background:white;
        color:black;
        font-weight:600;
        border:none;
    }

    </style>
    """, unsafe_allow_html=True)


    logo_url = "https://cdn-icons-png.flaticon.com/128/18111/18111997.png"


    col1, col2, col3 = st.columns([3,1,3])

    with col2:

        st.markdown('<div class="logo-container">', unsafe_allow_html=True)
        st.image(logo_url, width=170)
        st.markdown('</div>', unsafe_allow_html=True)


    st.markdown("<div class='title'>AI Nexus Studio v2</div>", unsafe_allow_html=True)


    left, center, right = st.columns([3,2,3])

    with center:

        menu = st.radio("Choose", ["Login", "Register"], horizontal=True)

        if menu == "Login":

            st.subheader("Login")

            with st.form("login_form"):

                email = st.text_input("Email", placeholder="Enter your email")

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Enter your password"
                )

                login_btn = st.form_submit_button(
                    "Login",
                    use_container_width=True
                )

                if login_btn:

                    if not email or not password:
                        st.warning("Please enter email and password")

                    else:

                        if login_user(email, password):

                            st.session_state.logged_in = True
                            st.session_state.email = email

                            st.success("Login Successful")
                            st.rerun()

                        else:
                            st.error("Invalid login credentials")

        else:

            st.subheader("Register")

            with st.form("register_form"):

                fullname = st.text_input(
                    "Full Name",
                    placeholder="Enter your full name"
                )

                email = st.text_input(
                    "Email Address",
                    placeholder="Enter your email"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Create a password"
                )

                register_btn = st.form_submit_button(
                    "Register",
                    use_container_width=True
                )

                if register_btn:

                    if not fullname or not email or not password:
                        st.warning("Please fill all fields")

                    else:

                        success = register_user(fullname, email, password)

                        if success:
                            st.success("Registration successful! Please login.")

                        else:
                            st.error("Email already exists")