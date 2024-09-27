import streamlit as st
import random
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_learning_resources():
    st.title("学习资源宝库")
    
    # 添加动画效果
    lottie_url = "https://assets5.lottiefiles.com/packages/lf20_v1yudlrx.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, speed=1, height=200, key="initial")

    resources = [
        {"title": "Python 奇妙之旅", "description": "从零开始的 Python 冒险", "link": "https://example.com/python-journey", "icon": "https://img.icons8.com/color/48/000000/python.png", "difficulty": "初级"},
        {"title": "数据分析魔法书", "description": "用 Pandas 揭秘数据的奥秘", "link": "https://example.com/data-magic", "icon": "https://img.icons8.com/color/48/000000/analytics.png", "difficulty": "中级"},
        {"title": "机器学习炼金术", "description": "将数据转化为智慧的艺术", "link": "https://example.com/ml-alchemy", "icon": "https://img.icons8.com/color/48/000000/machine-learning.png", "difficulty": "高级"},
        {"title": "Web开发魔法棒", "description": "挥一挥魔法棒，你的网站就出现了", "link": "https://example.com/web-magic", "icon": "https://img.icons8.com/color/48/000000/web.png", "difficulty": "中级"},
        {"title": "人工智能未来城", "description": "探索AI的无限可能", "link": "https://example.com/ai-future", "icon": "https://img.icons8.com/color/48/000000/artificial-intelligence.png", "difficulty": "高级"},
    ]
    
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        .resource-card {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 20px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 10px 10px 30px #d1d1d1, -10px -10px 30px #ffffff;
            transition: all 0.3s ease;
            font-family: 'Roboto', sans-serif;
        }
        .resource-card:hover {
            transform: translateY(-5px);
            box-shadow: 15px 15px 40px #d1d1d1, -15px -15px 40px #ffffff;
        }
        .resource-title {
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 15px;
            color: #333;
        }
        .resource-description {
            font-size: 16px;
            color: #666;
            margin-bottom: 15px;
            line-height: 1.5;
        }
        .resource-difficulty {
            font-size: 14px;
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 15px;
            display: inline-block;
            margin-bottom: 10px;
        }
        .difficulty-beginner { background-color: #a8e6cf; color: #1d3557; }
        .difficulty-intermediate { background-color: #ffd3b6; color: #7c3c21; }
        .difficulty-advanced { background-color: #ffaaa5; color: #6a040f; }
        .resource-link {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 25px;
            transition: background-color 0.3s ease;
        }
        .resource-link:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 添加搜索和筛选功能
    search_term = st.text_input("搜索资源", "")
    difficulty_filter = st.multiselect("按难度筛选", ["初级", "中级", "高级"])

    for resource in resources:
        if (search_term.lower() in resource['title'].lower() or search_term.lower() in resource['description'].lower()) and \
           (not difficulty_filter or resource['difficulty'] in difficulty_filter):
            difficulty_class = f"difficulty-{resource['difficulty'].lower()}"
            st.markdown(
                f"""
                <div class="resource-card">
                    <img src="{resource['icon']}" style="float: left; margin-right: 20px; width: 60px; height: 60px;">
                    <div class="resource-title">{resource['title']}</div>
                    <div class="resource-difficulty {difficulty_class}">{resource['difficulty']}</div>
                    <div class="resource-description">{resource['description']}</div>
                    <a class="resource-link" href="{resource['link']}" target="_blank">开启学习之旅</a>
                </div>
                """,
                unsafe_allow_html=True
            )

    # 添加互动性：随机推荐功能
    if st.button("随机推荐资源"):
        random_resource = random.choice(resources)
        st.success(f"推荐资源：{random_resource['title']} - {random_resource['description']}")

    # 添加用户反馈功能
    st.subheader("资源反馈")
    feedback = st.text_area("请分享您的学习体验或对资源的建议：")
    if st.button("提交反馈"):
        st.success("感谢您的反馈！我们会认真考虑您的建议。")

    # 添加学习进度追踪
    st.subheader("学习进度追踪")
    for resource in resources:
        progress = st.slider(f"{resource['title']} 学习进度", 0, 100, 0, key=resource['title'])
        if progress == 100:
            st.balloons()
            st.success(f"恭喜你完成 {resource['title']} 的学习！")

if __name__ == "__main__":
    render_learning_resources()
