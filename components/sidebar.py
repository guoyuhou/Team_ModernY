import streamlit as st
from streamlit_lottie import st_lottie
import requests
import random

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render():
    # 加载动画
    
    st.sidebar.markdown(
        """
        <div class="sidebar-header">
            <h3>导航</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 显示动画
    st_lottie(lottie_sidebar, height=80, key="sidebar")
    
    menu_items = {
        "首页": "home",
        "团队": "team_info",
        "创意": "product_dev",
        "学习": "learning_resources"
    }
    
    for key, value in menu_items.items():
        if st.sidebar.button(key, key=value):
            st.session_state.page = value
    
    st.sidebar.markdown("---")
    st.sidebar.info("版本: v2.0.0")
    
    # 添加互动元素
    user_idea = st.sidebar.text_input("创新灵感:")
    if st.sidebar.button("提交"):
        st.sidebar.balloons()
        st.sidebar.success("谢谢分享！")
    
    # 添加每日创新提示
    daily_tips = [
        "换个角度看问题",
        "头脑风暴",
        "读篇新技术文章",
        "15分钟冥想",
        "解决小技术难题"
    ]
    st.sidebar.markdown("---")
    st.sidebar.subheader("今日提示")
    st.sidebar.info(random.choice(daily_tips))
    
    # 添加创新进度追踪
    st.sidebar.markdown("---")
    st.sidebar.subheader("进度")
    progress = st.sidebar.slider("本周目标", 0, 100, 50)
    st.sidebar.progress(progress)
    
    # 添加快速笔记功能
    st.sidebar.markdown("---")
    st.sidebar.subheader("笔记")
    note = st.sidebar.text_area("灵感:", height=80)
    if st.sidebar.button("保存"):
        st.sidebar.success("已保存！")
    
    st.markdown(
        """
        <style>
        .sidebar-header {
            padding: 0.3rem;
            background: #f0f0f0;
            color: #333;
            text-align: center;
            margin-bottom: 0.3rem;
            border-radius: 3px;
        }
        .stButton>button {
            width: 100%;
            margin-bottom: 0.2rem;
            border: 1px solid #ddd;
            background: white;
            color: #333;
            transition: all 0.3s ease;
            border-radius: 3px;
            font-weight: normal;
            font-size: 0.8em;
            padding: 0.2rem;
        }
        .stButton>button:hover {
            background: #f0f0f0;
        }
        .sidebar .sidebar-content {
            background: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    return st.session_state.get('page', 'home')
