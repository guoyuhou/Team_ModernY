import streamlit as st

def render():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f0f2f6;
            color: #262730;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }
        </style>
        <div class="footer">
            © 2023 我们的团队. 保留所有权利.
        </div>
        """,
        unsafe_allow_html=True
    )
