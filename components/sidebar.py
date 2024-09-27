import streamlit as st

def render():
    st.sidebar.markdown(
        """
        <div class="sidebar-header">
            <h2>导航菜单</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    menu_items = {
        "首页": "home",
        "团队信息": "team_info",
        "产品开发流程": "product_dev",
        "学习资源": "learning_resources"
    }
    
    for key, value in menu_items.items():
        if st.sidebar.button(key, key=value):
            st.session_state.page = value
    
    st.sidebar.markdown("---")
    st.sidebar.info("当前版本: v1.0.0")
    
    st.markdown(
        """
        <style>
        .sidebar-header {
            padding: 1rem;
            background-color: #262730;
            color: white;
            text-align: center;
            margin-bottom: 1rem;
        }
        .stButton>button {
            width: 100%;
            margin-bottom: 0.5rem;
            border: none;
            background-color: #f0f2f6;
            color: #262730;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #e0e0e0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    return st.session_state.get('page', 'home')
