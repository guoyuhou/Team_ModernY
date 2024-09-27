import streamlit as st
from streamlit_lottie import st_lottie
import requests

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
    
    st.markdown(
        """
        <style>
        .sidebar-header {
            padding: 0.5rem;
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            color: white;
            text-align: center;
            margin-bottom: 0.5rem;
            border-radius: 5px;
        }
        .stButton>button {
            width: 100%;
            margin-bottom: 0.3rem;
            border: none;
            background: linear-gradient(45deg, #4CAF50, #45a049);
            color: white;
            transition: all 0.3s ease;
            border-radius: 10px;
            font-weight: bold;
            font-size: 0.9em;
            padding: 0.3rem;
        }
        .stButton>button:hover {
            transform: scale(1.02);
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #f8f9fa, #e9ecef);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    return st.session_state.get('page', 'home')
