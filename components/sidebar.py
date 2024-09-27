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
            <h2>创新导航</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 显示动画
    st_lottie(lottie_sidebar, height=150, key="sidebar")
    
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
    st.sidebar.success("创新版本: v2.0.0 - 突破边界")
    
    # 添加互动元素
    user_idea = st.sidebar.text_input("分享你的创新灵感:")
    if st.sidebar.button("提交灵感"):
        st.sidebar.balloons()
        st.sidebar.success("感谢你的创意贡献！")
    
    st.markdown(
        """
        <style>
        .sidebar-header {
            padding: 1rem;
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            color: white;
            text-align: center;
            margin-bottom: 1rem;
            border-radius: 10px;
        }
        .stButton>button {
            width: 100%;
            margin-bottom: 0.5rem;
            border: none;
            background: linear-gradient(45deg, #FF512F, #DD2476);
            color: white;
            transition: all 0.3s ease;
            border-radius: 20px;
            font-weight: bold;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #f8f9fa, #e9ecef);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    return st.session_state.get('page', 'home')
