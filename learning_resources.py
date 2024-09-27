import streamlit as st
from utils.db_utils import get_learning_resources

def load_learning_resources():
    return get_learning_resources()

def render_learning_resources():
    st.title("学习资源")
    
    resources = load_learning_resources()
    
    categories = list(set([r["category"] for r in resources]))
    selected_category = st.selectbox("选择类别", categories)
    
    filtered_resources = [r for r in resources if r["category"] == selected_category]
    
    for resource in filtered_resources:
        with st.expander(resource["title"]):
            st.write(resource["description"])
            st.write(f"难度: {resource['difficulty']}")
            st.write(f"估计学习时间: {resource['estimated_time']}")
            st.markdown(f"[开始学习]({resource['link']})")
    
    st.button("添加新资源", on_click=add_new_resource)

def add_new_resource():
    # 实现添加新资源的逻辑
    st.info("功能开发中...")

__all__ = ['render_learning_resources']

if __name__ == "__main__":
    render_learning_resources()
