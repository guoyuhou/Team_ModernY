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

def load_markdown_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), 'markdown', file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return markdown.markdown(content)
    except FileNotFoundError:
        return None

def render_learning_resources():
    st.title("学习资源宝库")
    
    if 'learning_page' not in st.session_state:
        st.session_state.learning_page = 'main'

    if st.session_state.learning_page == 'main':
        render_main_learning_page()
    else:
        content = load_markdown_file(st.session_state.learning_page)
        if content:
            if st.button("返回主页"):
                st.session_state.learning_page = 'main'
                st.experimental_rerun()
            st.markdown(content, unsafe_allow_html=True)
        else:
            st.error("抱歉，无法找到内容文件。我们正在努力修复这个问题。")
            if st.button("返回主页"):
                st.session_state.learning_page = 'main'

def render_main_learning_page():
    lottie_url = "https://assets5.lottiefiles.com/packages/lf20_v1yudlrx.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, speed=1, height=200, key="learning_lottie")

    resources = [
        {"title": "Streamlit框架+AI应用构建", "description": "学习如何使用Streamlit构建AI应用", "file": "streamlit_ai_tutorial.md", "icon": "https://img.icons8.com/color/48/000000/python.png", "difficulty": "中级"},
        {"title": "Django框架+AI应用搭建", "description": "使用Django框架搭建AI应用", "file": "django_ai_tutorial.md", "icon": "https://img.icons8.com/color/48/000000/django.png", "difficulty": "高级"},
        {"title": "Github使用教程", "description": "学习如何使用Github进行版本控制", "file": "github_tutorial.md", "icon": "https://img.icons8.com/color/48/000000/github.png", "difficulty": "初级"},
        {"title": "前端设计大全", "description": "全面学习前端设计技巧和最佳实践", "file": "frontend_design_tutorial.md", "icon": "https://img.icons8.com/color/48/000000/html-5.png", "difficulty": "中级"},
        {"title": "后端工具大全", "description": "探索各种后端开发工具和框架", "file": "backend_tools_tutorial.md", "icon": "https://img.icons8.com/color/48/000000/server.png", "difficulty": "高级"},
    ]

    for resource in resources:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(resource['icon'], width=60)
        with col2:
            st.subheader(resource['title'])
            st.write(resource['description'])
            st.write(f"难度：{resource['difficulty']}")
            if st.button(f"查看 {resource['title']} 内容", key=resource['title']):
                st.session_state.learning_page = resource['file']

if __name__ == "__main__":
    render_learning_resources()
