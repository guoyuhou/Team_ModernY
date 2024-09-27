import streamlit as st
import random

def render():
    # 创新元素：动态标语
    slogans = [
        "创新无界，未来无限",
        "激发灵感，引领变革",
        "跨界思维，创造奇迹",
        "科技融合，共创未来",
        "突破常规，定义明天"
    ]
    
    # 创新元素：动态颜色
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A", "#98D8C8"]
    
    st.markdown(
        f"""
        <div class="header">
            <div class="logo-container">
                <div class="logo-text">创新</div>
            </div>
            <h1 id="dynamic-slogan">{random.choice(slogans)}</h1>
        </div>
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');
        .header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: linear-gradient(45deg, #f3ec78, #af4261);
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .logo-container {{
            width: 60px;
            height: 60px;
            background-color: #fff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .logo-text {{
            font-family: 'Roboto', sans-serif;
            font-size: 1.2rem;
            font-weight: bold;
            color: #333;
        }}
        .header h1 {{
            color: #fff;
            font-size: 1.8rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            animation: colorChange 10s infinite;
        }}
        @keyframes colorChange {{
            0%, 100% {{ color: {colors[0]}; }}
            20% {{ color: {colors[1]}; }}
            40% {{ color: {colors[2]}; }}
            60% {{ color: {colors[3]}; }}
            80% {{ color: {colors[4]}; }}
        }}
        </style>
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
