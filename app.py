import streamlit as st
from pages import home, team_info, product_dev, learning_resources
from components import header, footer, sidebar

def main():
    st.set_page_config(page_title="团队内部平台", layout="wide")
    
    header.render()
    sidebar.render()
    
    page = st.sidebar.selectbox("选择页面", ["首页", "团队信息", "产品开发流程", "学习资源"])
    
    if page == "首页":
        home.render()
    elif page == "团队信息":
        team_info.render()
    elif page == "产品开发流程":
        product_dev.render()
    elif page == "学习资源":
        learning_resources.render()
    
    footer.render()

if __name__ == "__main__":
    main()
