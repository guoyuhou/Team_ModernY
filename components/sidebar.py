import streamlit as st
import random
from datetime import datetime

def render():
    st.sidebar.markdown(
        """
        <div class="sidebar-header">
            <h3>创新导航</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    menu_items = {
        "创新之家": "home",
        "梦想团队": "team_info",
        "创意工坊": "product_dev",
        "知识宝库": "learning_resources"
    }
    
    for key, value in menu_items.items():
        if st.sidebar.button(key, key=value, help=f"点击进入{key}"):
            st.session_state.page = value
    
    st.sidebar.markdown("---")
    st.sidebar.info("版本: v3.0.0 - 创新无限")
    
    # 添加互动元素
    user_idea = st.sidebar.text_input("闪现灵感:", placeholder="在这里分享你的创意...")
    if st.sidebar.button("点亮创意"):
        st.sidebar.balloons()
        st.sidebar.success("你的创意已被记录！继续保持创新精神！")
    
    # 添加每日创新提示
    daily_tips = [
        "尝试用不同的感官体验世界",
        "与一个陌生领域的专家交流",
        "挑战自己的固有观念",
        "在大自然中寻找设计灵感",
        "用音乐激发你的创造力"
    ]
    st.sidebar.markdown("---")
    st.sidebar.subheader("今日创新灵感")
    tip_of_the_day = random.choice(daily_tips)
    st.sidebar.info(tip_of_the_day)
    
    # 添加创新进度追踪
    st.sidebar.markdown("---")
    st.sidebar.subheader("创新进度")
    progress = st.sidebar.slider("本周创新目标", 0, 100, 50)
    progress_color = "green" if progress >= 80 else "orange" if progress >= 50 else "red"
    st.sidebar.markdown(
        f"""
        <div class="progress-bar" style="width: 100%; height: 20px; background-color: #f0f0f0; border-radius: 10px;">
            <div style="width: {progress}%; height: 100%; background-color: {progress_color}; border-radius: 10px; text-align: center; color: white;">
                {progress}%
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 添加快速笔记功能
    st.sidebar.markdown("---")
    st.sidebar.subheader("创意笔记")
    note = st.sidebar.text_area("记录你的灵感:", height=80, placeholder="在这里快速记录你的想法...")
    if st.sidebar.button("保存灵感"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.sidebar.success(f"灵感已保存！ ({timestamp})")
    
    # 添加创新挑战
    st.sidebar.markdown("---")
    st.sidebar.subheader("每日创新挑战")
    challenges = [
        "设计一个未来的交通工具",
        "发明一种新的环保材料",
        "创造一个解决日常问题的APP",
        "想象一种新的艺术形式",
        "构思一个改善教育的创新方案"
    ]
    daily_challenge = random.choice(challenges)
    st.sidebar.info(f"今日挑战：{daily_challenge}")
    
    st.markdown(
        """
        <style>
        .sidebar-header {
            padding: 0.5rem;
            background: linear-gradient(45deg, #6a11cb 0%, #2575fc 100%);
            color: white;
            text-align: center;
            margin-bottom: 0.5rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .stButton>button {
            width: 100%;
            margin-bottom: 0.3rem;
            border: none;
            background: linear-gradient(45deg, #FF512F 0%, #F09819 100%);
            color: white;
            transition: all 0.3s ease;
            border-radius: 5px;
            font-weight: bold;
            font-size: 0.9em;
            padding: 0.3rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #f6f9fc 0%, #ffffff 100%);
        }
        .progress-bar {
            transition: all 0.3s ease;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    return st.session_state.get('page', 'home')
