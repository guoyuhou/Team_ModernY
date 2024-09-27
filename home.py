import streamlit as st

def render_home():
    st.markdown(
        """
        <div class="welcome-section">
            <h1>欢迎来到我们的团队内部平台</h1>
            <p>我们是一个充满激情和创新的团队，致力于为客户提供最优质的服务。</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    try:
        # 静态数据
        team_data = {
            "description": "我们是一个充满激情和创新的团队，致力于为客户提供最优质的服务。",
            "vision": "成为行业内最受尊敬和信赖的技术解决方案提供商。",
            "values": [
                {"title": "创新", "description": "不断探索新技术"},
                {"title": "协作", "description": "团结一致，共创佳绩"},
                {"title": "诚信", "description": "诚实守信，言行一致"}
            ],
            "members": [
                {"department": "技术部"},
                {"department": "市场部"},
                {"department": "人力资源部"},
                {"department": "财务部"},
                {"department": "客户服务部"}
            ]
        }
        
        updates = [
            {
                "date": "2023-05-01",
                "title": "新产品发布",
                "content": "我们很高兴地宣布，我们的新产品已经成功上线！",
                "link": "https://example.com/new-product"
            },
            {
                "date": "2023-04-15",
                "title": "团队建设活动",
                "content": "上周末，我们组织了一次成功的团队建设活动，增进了团队成员之间的了解和信任。",
                "link": None
            }
        ]
        
        # 团队简介
        st.header("关于我们")
        st.write(team_data.get("description", "团队描述暂未提供"))
        
        # 团队愿景
        st.subheader("我们的愿景")
        st.info(team_data.get("vision", "团队愿景暂未提供"))
        
        # 核心价值观
        st.subheader("核心价值观")
        values = team_data.get("values", [])
        if values:
            cols = st.columns(len(values))
            for idx, value in enumerate(values):
                with cols[idx]:
                    st.metric(label=value.get("title", ""), value=value.get("description", ""))
        else:
            st.write("核心价值观暂未提供")
        
        # 最新动态
        st.header("最新动态")
        if updates:
            for update in updates:
                with st.expander(f"{update.get('date', '')} - {update.get('title', '')}"):
                    st.write(update.get("content", ""))
                    if update.get("link"):
                        st.markdown(f"[了解更多]({update['link']})")
        else:
            st.write("暂无最新动态")
        
        # 快速链接
        st.header("快速链接")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("查看团队信息"):
                st.session_state.page = "team_info"
        with col2:
            if st.button("浏览产品开发流程"):
                st.session_state.page = "product_dev"
        with col3:
            if st.button("访问学习资源"):
                st.session_state.page = "learning_resources"
        
        # 团队成员统计
        st.header("团队概况")
        members = team_data.get("members", [])
        total_members = len(members)
        departments = set(member.get("department", "") for member in members)
        
        col1, col2 = st.columns(2)
        col1.metric("团队成员总数", total_members)
        col2.metric("部门数量", len(departments))
        
    except Exception as e:
        st.error(f"加载页面时发生错误: {str(e)}")
        st.write("请检查数据格式是否正确。")

    # 添加一些视觉元素
    st.markdown(
        """
        <div class="feature-grid">
            <div class="feature-item">
                <img src="https://img.icons8.com/color/96/000000/innovation.png" alt="创新">
                <h3>创新</h3>
                <p>不断探索新技术</p>
            </div>
            <div class="feature-item">
                <img src="https://img.icons8.com/color/96/000000/collaboration.png" alt="协作">
                <h3>协作</h3>
                <p>团结一致，共创佳绩</p>
            </div>
            <div class="feature-item">
                <img src="https://img.icons8.com/color/96/000000/trust.png" alt="诚信">
                <h3>诚信</h3>
                <p>诚实守信，言行一致</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 添加CSS样式
    st.markdown(
        """
        <style>
        .welcome-section {
            background-color: #f0f2f6;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .welcome-section h1 {
            color: #262730;
        }
        .feature-grid {
            display: flex;
            justify-content: space-between;
            margin-top: 2rem;
        }
        .feature-item {
            text-align: center;
            padding: 1rem;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .feature-item img {
            width: 64px;
            height: 64px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    render_home()
