import streamlit as st
import random

def render():
    # 创新元素：每次刷新随机显示一条激励语
    inspirational_quotes = [
        "创新是进步的源泉",
        "突破常规，创造非凡",
        "用创意改变世界", 
        "今天的想象就是明天的现实",
        "创新始于好奇心"
    ]
    
    # 创新元素：添加社交媒体图标
    social_icons = """
    <a href="#" target="_blank"><i class="fab fa-weixin"></i></a>
    <a href="#" target="_blank"><i class="fab fa-weibo"></i></a>
    <a href="#" target="_blank"><i class="fab fa-github"></i></a>
    """
    
    st.markdown(
        f"""
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');
        .footer {{
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background: linear-gradient(90deg, #f0f2f6, #e6e9ef);
            color: #262730;
            text-align: center;
            padding: 15px 0;
            font-size: 14px;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
            z-index: 1000;
        }}
        .footer-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}
        .footer-quote {{
            font-style: italic;
            font-weight: bold;
        }}
        .footer-social a {{
            color: #262730;
            margin: 0 10px;
            font-size: 18px;
            transition: color 0.3s ease;
        }}
        .footer-social a:hover {{
            color: #4CAF50;
        }}
        @media (max-width: 768px) {{
            .footer-content {{
                flex-direction: column;
                gap: 10px;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        f"""
        <div class="footer">
            <div class="footer-content">
                <div class="footer-quote">{random.choice(inspirational_quotes)}</div>
                <div>© 2023 未来创新实验室. 激发灵感，创造未来。</div>
                <div class="footer-social">{social_icons}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
