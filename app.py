import streamlit as st
from dotenv import load_dotenv

from utils.ui_components import set_background
from auth.auth_db import create_table
from auth.auth_ui import auth_page

from modules.research_nexus import research_page
from modules.coding_nexus import coding_page
from modules.data_nexus import data_page
from modules.image_nexus import image_page
from modules.knowledge_chatbot import chatbot_page
from modules.prompt_playground import prompt_page

load_dotenv()

create_table()

st.set_page_config(
    page_title="AI Nexus Studio v2",
    page_icon="🤖",
    layout="wide"
)

set_background()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    auth_page()

else:

    with st.sidebar:

        st.image("https://cdn-icons-png.flaticon.com/128/18111/18111997.png", width=120)

        st.title("AI Nexus Studio v2")

        username = st.session_state.email.split("@")[0]
        st.success(f"Welcome {username}")

        menu = st.radio(
            "AI Tools",
            [
                "Dashboard",
                "Research Nexus",
                "Coding Nexus",
                "Data Analysis Nexus",
                "Image Analysis Nexus",
                "Knowledge Chatbot",
                "Prompt Playground"
            ]
        )

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    if menu == "Dashboard":

        st.title("🚀 AI Nexus Studio v2")

        st.markdown("### Multi-AI Copilot Platform")

        st.markdown(
        "A unified AI platform where **multiple copilots** help with research, coding, "
        "data analysis, image understanding, chat interaction, and prompt engineering."
        )

        col1,col2,col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="ai-card">
            <h4>🔎 Research Nexus</h4>
            <p>Generate academic-style AI research summaries including concepts,
            trends, applications and recommended research papers.</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="ai-card">
            <h4>💻 Coding Nexus</h4>
            <p>An AI coding assistant that explains problems, writes optimized code,
            shows examples and explains best practices.</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="ai-card">
            <h4>📊 Data Analysis Nexus</h4>
            <p>Upload datasets and automatically generate statistics,
            visualizations and machine-learning insights.</p>
            </div>
            """, unsafe_allow_html=True)

        col4,col5,col6 = st.columns(3)

        with col4:
            st.markdown("""
            <div class="ai-card">
            <h4>🖼 Image Analysis Nexus</h4>
            <p>AI powered computer vision tool that analyzes uploaded
            images and explains objects, scenes and activities.</p>
            </div>
            """, unsafe_allow_html=True)

        with col5:
            st.markdown("""
            <div class="ai-card">
            <h4>💬 Knowledge Chatbot</h4>
            <p>Interactive conversational AI assistant that answers
            questions and explains concepts using Gemini AI.</p>
            </div>
            """, unsafe_allow_html=True)

        with col6:
            st.markdown("""
            <div class="ai-card">
            <h4>🧠 Prompt Playground</h4>
            <p>Experiment with prompt engineering techniques such as
            optimization, rewriting and explanation.</p>
            </div>
            """, unsafe_allow_html=True)

    elif menu == "Research Nexus":
        research_page()

    elif menu == "Coding Nexus":
        coding_page()

    elif menu == "Data Analysis Nexus":
        data_page()

    elif menu == "Image Analysis Nexus":
        image_page()

    elif menu == "Knowledge Chatbot":
        chatbot_page()

    elif menu == "Prompt Playground":
        prompt_page()