import streamlit as st
from utils.gemini_client import ask_gemini


def prompt_page():

    st.title("🧠 Prompt Playground")

    st.markdown("Experiment with Prompt Engineering techniques.")

    prompt = st.text_area("Enter your prompt")

    task = st.selectbox(
        "Choose Action",
        [
            "Prompt Optimization",
            "Prompt Rewrite",
            "Prompt Explanation"
        ]
    )

    if st.button("Run Prompt"):

        if task == "Prompt Optimization":

            query = f"""
            Optimize the following prompt to produce better AI responses:

            {prompt}

            Improve clarity, structure, and specificity.
            """

        elif task == "Prompt Rewrite":

            query = f"""
            Rewrite this prompt to make it more effective:

            {prompt}
            """

        else:

            query = f"""
            Explain what this prompt is trying to achieve:

            {prompt}
            """

        with st.spinner("🧠 AI analyzing prompt..."):
            result = ask_gemini(query)

        st.markdown(result)