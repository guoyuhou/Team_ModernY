import streamlit as st
import random

def render_home():

    # 欢迎部分
    st.markdown(
        """
        <div class="welcome-section">
            <h1>欢迎来到未来创新实验室</h1>
            <p>在这里，我们不仅激发灵感，更是创造未来的先锋。</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    try:
        # 动态数据
        team_data = {
            "description": "我们是一群跨界创新者，融合科技、艺术与人文，致力于塑造更美好的未来。",
            "vision": "成为引领全球创新生态系统的先驱力量。",
            "values": [
                {"title": "突破边界", "description": "挑战常规，创造不可能", "icon": "🚀"},
                {"title": "共创共赢", "description": "开放协作，激发无限可能", "icon": "🤝"},
                {"title": "责任创新", "description": "以人为本，科技向善", "icon": "🌟"},
                {"title": "持续学习", "description": "拥抱变化，永不止步", "icon": "🧠"}
            ],
            "members": [
                {"department": "前沿科技研究院"},
                {"department": "创意设计工作室"},
                {"department": "用户体验实验室"},
                {"department": "可持续发展中心"},
                {"department": "跨界创新孵化器"}
            ]
        }
        
        updates = [
            {
                "date": "2023-05-15",
                "title": "突破性AI模型发布",
                "content": "我们的最新AI模型在理解人类情感方面取得重大突破，为人机交互开辟新纪元！",
                "link": "https://example.com/ai-breakthrough"
            },
            {
                "date": "2023-05-01",
                "title": "全球创新马拉松",
                "content": "我们成功举办了一场48小时不间断的全球创新马拉松，来自50个国家的参与者共同探索未来城市解决方案。",
                "link": "https://example.com/innovation-marathon"
            }
        ]
        
        # 团队简介
        st.header("我们的使命")
        st.markdown(f"<p class='team-description'>{team_data.get('description', '团队描述暂未提供')}</p>", unsafe_allow_html=True)
        
        # 团队愿景
        st.subheader("愿景")
        st.info(team_data.get("vision", "团队愿景暂未提供"))
        
        # 核心价值观
        st.subheader("核心价值观")
        values = team_data.get("values", [])
        if values:
            cols = st.columns(len(values))
            for idx, value in enumerate(values):
                with cols[idx]:
                    st.markdown(f"<div class='value-card'><h3>{value['icon']} {value.get('title', '')}</h3><p>{value.get('description', '')}</p></div>", unsafe_allow_html=True)
        else:
            st.write("核心价值观暂未提供")
        
        # 创新指数
        st.header("创新指数")
        innovation_index = random.randint(80, 100)
        st.progress(innovation_index)
        st.markdown(f"<p class='innovation-index'>当前创新指数: {innovation_index}%</p>", unsafe_allow_html=True)
        
        # 最新动态
        st.header("突破性进展")
        if updates:
            for update in updates:
                with st.expander(f"{update.get('date', '')} - {update.get('title', '')}"):
                    st.markdown(f"<p class='update-content'>{update.get('content', '')}</p>", unsafe_allow_html=True)
                    if update.get("link"):
                        st.markdown(f"<a href='{update['link']}' target='_blank' class='learn-more-btn'>深入探索</a>", unsafe_allow_html=True)
        else:
            st.write("暂无最新动态")
        
        # 互动环节
        st.header("参与创新")
        user_idea = st.text_area("分享你的创新想法：")
        if st.button("提交想法"):
            st.success("感谢你的贡献！我们的创新团队将认真评估你的想法。")
        
        # 快速链接
        st.header("探索更多")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("🧬 前沿研究"):
                st.session_state.page = "frontier_research"
        with col2:
            if st.button("🎨 创意工坊"):
                st.session_state.page = "creative_workshop"
        with col3:
            if st.button("🌍 可持续项目"):
                st.session_state.page = "sustainable_projects"
        with col4:
            if st.button("🚀 创新孵化器"):
                st.session_state.page = "innovation_incubator"
        
        # 团队成员统计
        st.header("创新生态系统")
        members = team_data.get("members", [])
        total_members = len(members)
        departments = set(member.get("department", "") for member in members)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("创新先锋", total_members, "持续增长")
        col2.metric("跨界部门", len(departments), "多元融合")
        col3.metric("全球合作伙伴", random.randint(50, 100), "不断扩大")
        
    except Exception as e:
        st.error(f"创新过程中遇到了一些挑战: {str(e)}")
        st.write("别担心，这正是我们突破自我的机会！")

    # 添加CSS样式
    st.markdown(
        """
        <style>
        .welcome-section {
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        .welcome-section h1 {
            font-size: 2.8rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .team-description {
            font-size: 1.3rem;
            line-height: 1.7;
            color: #333;
            background: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        .value-card {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .value-card:hover {
            transform: translateY(-10px) scale(1.05);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }
        .update-content {
            font-size: 1.1rem;
            line-height: 1.6;
            color: #333;
        }
        .learn-more-btn {
            display: inline-block;
            margin-top: 15px;
            padding: 8px 20px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 30px;
            transition: all 0.3s ease;
            font-weight: bold;
        }
        .learn-more-btn:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        .stButton>button {
            width: 100%;
            border-radius: 30px;
            font-weight: bold;
            transition: all 0.3s ease;
            background-color: #3498db;
            color: white;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background-color: #2980b9;
        }
        .innovation-index {
            font-size: 1.5rem;
            font-weight: bold;
            color: #3498db;
            text-align: center;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    render_home()
