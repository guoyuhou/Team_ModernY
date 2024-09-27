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
    lottie_sidebar = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_jtbfg2nb.json")
    
    st.sidebar.markdown(
        """
        <div class="sidebar-header">
            <h3>创新导航</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 显示动画
    st_lottie(lottie_sidebar, height=100, key="sidebar")
    
    menu_items = {
        "创新中心": "home",
        "先锋团队": "team_info",
        "创意孵化": "product_dev",
        "知识宝库": "learning_resources"
    }
    
    for key, value in menu_items.items():
        if st.sidebar.button(key, key=value):
            st.session_state.page = value
    
    st.sidebar.markdown("---")
    st.sidebar.info("创新版本: v2.0.0 - 突破边界")
    
    # 添加互动元素
    user_idea = st.sidebar.text_input("分享你的创新灵感:")
    if st.sidebar.button("提交灵感"):
        st.sidebar.balloons()
        st.sidebar.success("感谢你的创意贡献！")
    
    # 添加每日创新提示
    daily_tips = [
        "尝试从不同角度看问题",
        "与团队成员进行头脑风暴",
        "阅读一篇关于新兴技术的文章",
        "花15分钟冥想，让思维放空",
        "尝试解决一个小的技术挑战"
    ]
    st.sidebar.markdown("---")
    st.sidebar.subheader("每日创新提示")
    st.sidebar.info(random.choice(daily_tips))
    
    # 添加创新进度追踪
    st.sidebar.markdown("---")
    st.sidebar.subheader("创新进度")
    progress = st.sidebar.slider("本周创新目标完成度", 0, 100, 50)
    st.sidebar.progress(progress)
    
    # 添加快速笔记功能
    st.sidebar.markdown("---")
    st.sidebar.subheader("快速笔记")
    note = st.sidebar.text_area("记录你的灵感:", height=100)
    if st.sidebar.button("保存笔记"):
        # 这里可以添加保存笔记的逻辑
        st.sidebar.success("笔记已保存！")
    
    st.markdown(
        """
        <style>
        .sidebar-header {
            padding: 0.5rem;
            background: #f0f0f0;
            color: #333;
            text-align: center;
            margin-bottom: 0.5rem;
            border-radius: 5px;
        }
        .stButton>button {
            width: 100%;
            margin-bottom: 0.3rem;
            border: 1px solid #ddd;
            background: white;
            color: #333;
            transition: all 0.3s ease;
            border-radius: 5px;
            font-weight: normal;
            font-size: 0.9em;
            padding: 0.3rem;
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
