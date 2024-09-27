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
            transition: background-color 0.5s ease;
        }
        .stButton>button {
            width: 100%;
            background-color: #ffffff;
            color: #000000;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            margin-bottom: 10px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        .stButton>button:hover {
            background-color: #f0f0f0;
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stButton>button::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 5px;
            height: 5px;
            background: rgba(255, 255, 255, 0.5);
            opacity: 0;
            border-radius: 100%;
            transform: scale(1, 1) translate(-50%);
            transform-origin: 50% 50%;
        }
        .stButton>button:hover::after {
            animation: ripple 1s ease-out;
        }
        @keyframes ripple {
            0% {
                transform: scale(0, 0);
                opacity: 1;
            }
            20% {
                transform: scale(25, 25);
                opacity: 1;
            }
            100% {
                opacity: 0;
                transform: scale(40, 40);
            }
        }
        .sidebar .sidebar-content {
            animation: sidebarFadeIn 1s ease-out;
        }
        @keyframes sidebarFadeIn {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        </style>
        <script>
        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              entry.target.style.animation = 'fadeInUp 0.5s ease-out forwards';
            }
          });
        }, { threshold: 0.1 });

        document.querySelectorAll('.sidebar .sidebar-content > *').forEach(el => {
          observer.observe(el);
        });

        function animateProgress() {
          const progress = document.querySelector('.stProgress > div');
          let width = 0;
          const interval = setInterval(() => {
            if (width >= progress.style.width.replace('%', '')) {
              clearInterval(interval);
            } else {
              width++;
              progress.style.width = width + '%';
            }
          }, 10);
        }

        document.addEventListener('DOMContentLoaded', (event) => {
          animateProgress();
        });
        </script>
        """,
        unsafe_allow_html=True
    )

    return st.session_state.get('page', 'home')
