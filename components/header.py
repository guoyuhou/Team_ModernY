import streamlit as st

def render():
    st.image("static/images/logo.png", width=200)
    st.markdown(
        """
        <style>
        .stApp header {
            background-color: #f0f2f6;
            padding: 1rem;
            border-bottom: 1px solid #e0e0e0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
