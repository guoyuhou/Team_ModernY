import streamlit as st
from components import header, sidebar, footer
import home, team_info, product_dev
from learning_resources import render_learning_resources

def main():
    st.set_page_config(page_title="ModernY平台", layout="wide")
    
    # 添加加载动画
    with st.spinner("正在加载..."):
        header.render()
        
        # 获取侧边栏选择的页面，并设置默认值
        page = sidebar.render()
        if page is None:
            page = "home"  # 设置默认页面
        
        # 使用字典来映射页面名称和对应的渲染函数
        page_functions = {
            "home": home.render_home,
            "team_info": team_info.render_team_info,
            "product_dev": product_dev.render_product_dev,
            "learning_resources": render_learning_resources
        }
        
        # 如果页面存在于字典中，则调用对应的函数
        if page in page_functions:
            page_functions[page]()
        else:
            st.error(f"未知的页面: {page}")
        
        footer.render()

    # 添加全局样式
    st.markdown(
        """
        <style>
        body {
            color: #333;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }
        .stButton>button {
            border-radius: 20px;
            border: 1px solid #4CAF50;
            background-color: white;
            color: #4CAF50;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #4CAF50;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
