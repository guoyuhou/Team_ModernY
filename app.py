import streamlit as st
from home import render_home
from team_info import render_team_info
from product_dev import render_product_dev
from learning_resources import render_learning_resources
from components import header, footer, sidebar

def main():
    st.set_page_config(page_title="团队内部平台", layout="wide")
    
    header.render()
    sidebar.render()
    
    page = st.sidebar.selectbox("选择页面", ["首页", "团队信息", "产品开发流程", "学习资源"])
    
    if page == "首页":
        render_home()
    elif page == "团队信息":
        render_team_info()
    elif page == "产品开发流程":
        render_product_dev()
    elif page == "学习资源":
        render_learning_resources()
    
    footer.render()

if __name__ == "__main__":
    main()
