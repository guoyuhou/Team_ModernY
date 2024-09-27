import streamlit as st

def render():
    # 使用在线图片URL替代本地图片
    logo_url = "https://img.freepik.com/free-vector/flat-design-ac-logo-template_23-2149282639.jpg"
    
    try:
        # 直接使用st.image加载在线图片
        st.image(logo_url, width=200)
    except Exception as e:
        st.error(f"无法加载logo图片: {str(e)}")
        # 使用文本替代logo
        st.title("团队内部平台")
    
    st.markdown(
        """
        <style>
        .stApp header {
            background-color: #f0f2f6;
            padding: 1rem;
            border-bottom: 1px solid #e0e0e0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
