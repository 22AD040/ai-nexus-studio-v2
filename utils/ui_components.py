import streamlit as st
from config import BACKGROUND_URL

def set_background():

    st.markdown(
        f"""
        <style>

        /* BACKGROUND */

        .stApp {{
        background-image: url("{BACKGROUND_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        }}

        .stApp::before {{
        content:"";
        position:fixed;
        top:0;
        left:0;
        width:100%;
        height:100%;
        background:rgba(0,0,0,0.75);
        z-index:-1;
        }}

        /* SIDEBAR */

        section[data-testid="stSidebar"] {{
        background:rgba(2,6,23,0.96);
        }}

        /* SIDEBAR MENU TEXT WHITE */

        section[data-testid="stSidebar"] div[role="radiogroup"] label p,
        section[data-testid="stSidebar"] div[role="radiogroup"] label span{{
        color:white !important;
        font-weight:500 !important;
        }}

        section[data-testid="stSidebar"] {{
        color:white !important;
        }}

        section[data-testid="stSidebar"] h1 {{
        color:#ffffff !important;
        font-weight:800 !important;
        }}

        /* HEADINGS */

        h1,h2,h3,h4,h5,h6 {{
        color:white !important;
        }}

        /* LABELS */

        label {{
        color:white !important;
        font-weight:600;
        }}

        /* TEXT OUTPUT */

        .stMarkdown p,
        .stMarkdown span,
        .stMarkdown div,
        .stMarkdown li,
        .stText {{
        color:#e2e8f0 !important;
        font-size:15px;
        }}

        /* AI GENERATED OUTPUT */

        .stMarkdown h1,
        .stMarkdown h2,
        .stMarkdown h3 {{
        color:white !important;
        }}

        /* CODE BLOCKS */

        pre {{
        background:#020617 !important;
        color:#38bdf8 !important;
        border-radius:8px;
        }}

        /* BUTTONS */

        .stButton button {{
        background:white !important;
        color:black !important;
        font-weight:700 !important;
        border-radius:8px;
        }}

        /* INPUT BOXES */

        textarea,
        input,
        .stTextInput input,
        .stTextArea textarea {{
        background:white !important;
        color:black !important;
        border-radius:8px;
        }}

        /* FILE UPLOADER */

        section[data-testid="stFileUploader"] {{
        background:white !important;
        border-radius:8px;
        }}

        section[data-testid="stFileUploader"] * {{
        color:black !important;
        }}

        /* SELECT BOX */

        div[data-baseweb="select"] {{
        background:white !important;
        }}

        div[data-baseweb="select"] * {{
        color:black !important;
        }}

        /* CHAT INPUT */

        div[data-testid="stChatInput"] textarea {{
        background:white !important;
        color:black !important;
        }}

        /* SPINNER TEXT */

        .stSpinner {{
        color:white !important;
        }}

        /* DASHBOARD CARDS */

        .ai-card {{
        background:rgba(2,6,23,0.88);
        padding:26px;
        border-radius:14px;
        backdrop-filter: blur(10px);
        border:1px solid rgba(255,255,255,0.1);
        height:200px;
        display:flex;
        flex-direction:column;
        justify-content:center;
        }}

        .ai-card h4 {{
        color:#38bdf8;
        font-size:22px;
        font-weight:700;
        }}

        .ai-card p {{
        color:#e2e8f0;
        }}

        /* ----------------- ADDED FIXES ----------------- */

        /* RADIO BUTTON TEXT (Login/Register) */

        div[role="radiogroup"] label span{{
        color:white !important;
        font-weight:600 !important;
        }}

        /* LOGOUT BUTTON TEXT FIX */

        .stButton button{{
        background:white !important;
        color:black !important;
        }}

        /* FILE NAME (UPLOADED DATASET) */

        section[data-testid="stFileUploader"] span{{
        color:white !important;
        font-weight:500;
        }}

        /* SUCCESS MESSAGE (Green Box) */

        .stSuccess{{
        color:white !important;
        font-weight:600;
        }}

        /* INFO MESSAGE (Blue Box) */

        .stInfo{{
        color:white !important;
        font-weight:600;
        }}

        /* DATAFRAME TEXT VISIBILITY */

        .stDataFrame{{
        color:white !important;
        }}

        /* ALERT TEXT */

        .stAlert{{
        color:white !important;
        }}

        /* DATASET FILE TEXT */

        [data-testid="stFileUploader"] div{{
        color:white !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )