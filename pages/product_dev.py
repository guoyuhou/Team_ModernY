import streamlit as st
from utils.db_utils import get_dev_process
from utils.cache_utils import cache_data

@cache_data(ttl=3600)
def load_dev_process():
    return get_dev_process()

def render_product_dev():
    st.title("产品开发流程")
    
    dev_process = load_dev_process()
    
    for stage in dev_process:
        st.header(stage["name"])
        st.write(stage["description"])
        
        for step in stage["steps"]:
            st.subheader(step["title"])
            st.write(step["content"])
            
            if "tools" in step:
                st.write("推荐工具:")
                for tool in step["tools"]:
                    st.write(f"- {tool}")
        
        st.write("---")
    
    st.button("开始新项目", on_click=start_new_project)

def start_new_project():
    # 实现开始新项目的逻辑
    st.success("新项目已创建!")

__all__ = ['render_product_dev']

if __name__ == "__main__":
    render_product_dev()
