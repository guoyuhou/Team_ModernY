import streamlit as st
import requests
from io import BytesIO

def render():
    # 从网上获取一个示例logo图片
    logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Streamlit-logo-primary-colormark-darktext.png/320px-Streamlit-logo-primary-colormark-darktext.png"
    response = requests.get(logo_url)
    logo_image = BytesIO(response.content)
    
    st.image(logo_image, width=200)
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
