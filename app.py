import streamlit as st
from components import header, sidebar, footer
import home, team_info, product_dev, learning_resources

def main():
    st.set_page_config(page_title="团队内部平台", layout="wide")
    
    # 添加加载动画
    with st.spinner("正在加载..."):
        header.render()
        
        page = sidebar.render()
        
        if page == "home":
            home.render_home()
        elif page == "team_info":
            team_info.render_team_info()
        elif page == "product_dev":
            product_dev.render_product_dev()
        elif page == "learning_resources":
            learning_resources.render_learning_resources()
        
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
