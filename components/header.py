import streamlit as st

def render():
    # 使用更符合团队主题的在线图片URL
    logo_url = "https://img.freepik.com/free-vector/gradient-technology-logo-template_23-2149217425.jpg"
    
    st.markdown(
        f"""
        <div class="header">
            <img src="{logo_url}" alt="团队logo" class="logo">
            <h1>我们的创新团队</h1>
        </div>
        <style>
        .header {{
            display: flex;
            align-items: center;
            background-color: #f0f2f6;
            padding: 1rem;
            border-bottom: 1px solid #e0e0e0;
        }}
        .logo {{
            width: 50px;
            margin-right: 1rem;
        }}
        .header h1 {{
            color: #262730;
            font-size: 1.5rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
