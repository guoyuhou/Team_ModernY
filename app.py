import streamlit as st
from home import render_home
from team_info import render_team_info
from product_dev import render_product_dev
from learning_resources import render_learning_resources
from components import header, footer, sidebar

def main():
    st.set_page_config(page_title="团队内部平台", layout="wide")
    
    header.render()
    
    page = sidebar.render()
    
    if page == "home":
        render_home()
    elif page == "team_info":
        render_team_info()
    elif page == "product_dev":
        render_product_dev()
    elif page == "learning_resources":
        render_learning_resources()
    
    footer.render()

if __name__ == "__main__":
    main()
