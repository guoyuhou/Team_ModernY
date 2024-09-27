import streamlit as st
import random

def render():
    # 创新元素：动态标语
    slogans = [
        "创新无界，未来无限",
        "激发灵感，引领变革",
        "跨界思维，创造奇迹",
        "突破常规，定义明天"
    ]
    
    # 创新元素：动态颜色
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A", "#98D8C8"]
    st.markdown(
        f"""
        <style>
        .welcome-section {{
            text-align: center;
            padding: 2rem;
            background: linear-gradient(45deg, #f3ec78, #af4261);
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .welcome-section h1 {{
            color: #fff;
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        .welcome-section p {{
            color: #fff;
            font-size: 1.2rem;
            font-weight: bold;
        }}
        @keyframes colorChange {{
            0%, 100% {{ color: {colors[0]}; }}
            20% {{ color: {colors[1]}; }}
            40% {{ color: {colors[2]}; }}
            60% {{ color: {colors[3]}; }}
            80% {{ color: {colors[4]}; }}
        }}
        <script>
        function changeSlogan() {{
            const slogans = {slogans};
            const slogan = document.getElementById('dynamic-slogan');
            setInterval(() => {{
                slogan.textContent = slogans[Math.floor(Math.random() * slogans.length)];
            }}, 5000);
        }}
        changeSlogan();
        </script>
        """,
        unsafe_allow_html=True
    )
