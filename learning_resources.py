import streamlit as st

# 移除这行：
# from utils.db_utils import get_learning_resources

def render_learning_resources():
    st.title("学习资源")
    
    resources = [
        {"title": "Python 基础教程", "description": "适合初学者的 Python 教程", "link": "https://example.com/python-basics", "icon": "https://img.icons8.com/color/48/000000/python.png"},
        {"title": "数据分析入门", "description": "使用 Pandas 进行数据分析", "link": "https://example.com/data-analysis", "icon": "https://img.icons8.com/color/48/000000/analytics.png"},
        {"title": "机器学习基础", "description": "机器学习算法介绍", "link": "https://example.com/ml-basics", "icon": "https://img.icons8.com/color/48/000000/machine-learning.png"},
    ]
    
    st.markdown(
        """
        <style>
        .resource-card {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .resource-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .resource-description {
            font-size: 14px;
            color: #666;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    for resource in resources:
        st.markdown(
            f"""
            <div class="resource-card">
                <img src="{resource['icon']}" style="float: left; margin-right: 15px; width: 48px; height: 48px;">
                <div class="resource-title">{resource['title']}</div>
                <div class="resource-description">{resource['description']}</div>
                <a href="{resource['link']}" target="_blank">了解更多</a>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    render_learning_resources()
