import streamlit as st
import random
from streamlit_lottie import st_lottie
import requests
import markdown
import os

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_markdown_page(content):
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    if st.button("返回"):
        st.session_state.page = "main"
        st.empty()
        render_learning_resources()
    st.markdown(content, unsafe_allow_html=True)

def render_learning_resources():
    if "page" not in st.session_state:
        st.session_state.page = "main"

    # 创建一个空的容器来放置页面内容
    page_container = st.empty()

    with page_container.container():
        if st.session_state.page == "main":
            render_main_page()
        else:
            file_path = os.path.join(os.path.dirname(__file__), 'markdown', st.session_state.page)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    html = markdown.markdown(content)
                    render_markdown_page(html)
            except FileNotFoundError:
                st.error(f"抱歉，无法找到内容文件。我们正在努力修复这个问题。")
                if st.button("返回主页"):
                    st.session_state.page = "main"
                    page_container.empty()
                    render_learning_resources()

def render_main_page():
    st.title("学习资源宝库")
    
    # 添加动画效果
    lottie_url = "https://assets5.lottiefiles.com/packages/lf20_v1yudlrx.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, speed=1, height=200, key="initial")

    resources = [
        {"title": "Streamlit框架+AI应用构建", "description": "学习如何使用Streamlit构建AI应用", "file": "streamlit_ai_tutorial.md", "icon": "https://img.icons8.com/color/48/000000/python.png", "difficulty": "中级"},
        {"title": "Django框架+AI应用搭建", "description": "使用Django框架搭建AI应用", "file": "django_ai_tutorial.md", "icon": "https://img.icons8.com/color/48/000000/django.png", "difficulty": "高级"},
        {"title": "Github使用教程", "description": "学习如何使用Github进行版本控制", "file": "github_tutorial.md", "icon": "https://img.icons8.com/color/48/000000/github.png", "difficulty": "初级"},
    ]
    
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        .resource-card {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 20px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 10px 10px 30px #d1d1d1, -10px -10px 30px #ffffff;
            transition: all 0.3s ease;
            font-family: 'Roboto', sans-serif;
        }
        .resource-card:hover {
            transform: translateY(-5px);
            box-shadow: 15px 15px 40px #d1d1d1, -15px -15px 40px #ffffff;
        }
        .resource-title {
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 15px;
            color: #333;
        }
        .resource-description {
            font-size: 16px;
            color: #666;
            margin-bottom: 15px;
            line-height: 1.5;
        }
        .resource-difficulty {
            font-size: 14px;
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 15px;
            display: inline-block;
            margin-bottom: 10px;
        }
        .difficulty-beginner { background-color: #a8e6cf; color: #1d3557; }
        .difficulty-intermediate { background-color: #ffd3b6; color: #7c3c21; }
        .difficulty-advanced { background-color: #ffaaa5; color: #6a040f; }
        .resource-link {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 25px;
            transition: background-color 0.3s ease;
        }
        .resource-link:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    for resource in resources:
        difficulty_class = f"difficulty-{resource['difficulty'].lower()}"
        st.markdown(
            f"""
            <div class="resource-card">
                <img src="{resource['icon']}" style="float: left; margin-right: 20px; width: 60px; height: 60px;">
                <div class="resource-title">{resource['title']}</div>
                <div class="resource-difficulty {difficulty_class}">{resource['difficulty']}</div>
                <div class="resource-description">{resource['description']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button(f"查看 {resource['title']} 内容", key=resource['title']):
            st.session_state.page = resource['file']
            st.empty()
            render_learning_resources()

if __name__ == "__main__":
    render_learning_resources()
