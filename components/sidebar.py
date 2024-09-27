import streamlit as st
import random

def render():
    st.sidebar.title("创新导航")
    
    menu_items = {
        "创新之家": "home",
        "梦想团队": "team_info",
        "创意工坊": "product_dev",
        "知识宝库": "learning_resources"
    }
    
    for key, value in menu_items.items():
        if st.sidebar.button(key, key=value):
            st.session_state.page = value
    
    st.sidebar.markdown("---")
    st.sidebar.caption("版本: v3.0.0 - 创新无限")
    
    # 每日创新提示
    daily_tips = [
        "尝试用不同的感官体验世界",
        "与一个陌生领域的专家交流",
        "挑战自己的固有观念",
        "在大自然中寻找设计灵感",
        "用音乐激发你的创造力"
    ]
    st.sidebar.markdown("---")
    st.sidebar.subheader("今日创新灵感")
    tip_of_day = random.choice(daily_tips)
    st.sidebar.info(tip_of_day)
    
    # 创新进度追踪
    st.sidebar.markdown("---")
    st.sidebar.subheader("创新进度")
    progress = st.sidebar.slider("本周创新目标", 0, 100, 50)
    st.sidebar.progress(progress)
    
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
        }
        .stButton>button {
            width: 100%;
            background-color: #ffffff;
            color: #000000;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            margin-bottom: 10px;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #f0f0f0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    return st.session_state.get('page', 'home')
