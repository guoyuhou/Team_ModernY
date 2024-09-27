import streamlit as st

def render():
    st.sidebar.title("导航")
    
    menu_items = {
        "首页": "home",
        "团队信息": "team_info",
        "产品开发流程": "product_dev",
        "学习资源": "learning_resources"
    }
    
    selected = st.sidebar.radio("选择页面", list(menu_items.keys()))
    
    st.sidebar.markdown("---")
    st.sidebar.info("当前版本: v1.0.0")
    
    return menu_items[selected]
