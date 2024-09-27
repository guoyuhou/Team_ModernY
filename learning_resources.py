import streamlit as st

# 移除这行：
# from utils.db_utils import get_learning_resources

def render_learning_resources():
    st.title("学习资源")
    
    # 使用静态数据替代数据库查询
    resources = [
        {"title": "Python 基础教程", "description": "适合初学者的 Python 教程", "link": "https://example.com/python-basics"},
        {"title": "数据分析入门", "description": "使用 Pandas 进行数据分析", "link": "https://example.com/data-analysis"},
        {"title": "机器学习基础", "description": "机器学习算法介绍", "link": "https://example.com/ml-basics"},
    ]
    
    for resource in resources:
        with st.expander(resource["title"]):
            st.write(resource["description"])
            st.markdown(f"[了解更多]({resource['link']})")

if __name__ == "__main__":
    render_learning_resources()
