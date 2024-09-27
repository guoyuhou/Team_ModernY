import streamlit as st
import random
import time
import plotly.graph_objects as go

def render_home():
    # 欢迎界面
    st.markdown(
        """
        <div class="welcome-section">
            <h1>ModernY</h1>
            <p class="subtitle">在这里，我们不仅激发灵感，更是创造未来的先锋。</p>
            <div class="scroll-down"></div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    try:
        # 动态数据
        team_data = {
            "description": "我们是一群跨界创新者，融合科技、艺术与人文，致力于塑造更美好的未来。我们相信，真正的创新源于多元思维的碰撞和跨界合作的力量。",
            "vision": "成为引领全球创新生态系统的先驱力量，推动人类文明向更高远的未来迈进。",
            "values": [
                {"title": "突破边界", "description": "挑战常规，创造不可能", "icon": "🚀", "color": "#FF6B6B"},
                {"title": "共创共赢", "description": "开放协作，激发无限可能", "icon": "🤝", "color": "#4ECDC4"},
                {"title": "责任创新", "description": "以人为本，科技向善", "icon": "🌟", "color": "#45B7D1"},
                {"title": "持续学习", "description": "拥抱变化，永不止步", "icon": "🧠", "color": "#FFA07A"},
                {"title": "跨界融合", "description": "打破壁垒，创造奇迹", "icon": "🌈", "color": "#98D8C8"}
            ],
            "members": [
                {"department": "前沿科技研究院", "count": random.randint(20, 50)},
                {"department": "创意设计工作室", "count": random.randint(15, 40)},
                {"department": "用户体验实验室", "count": random.randint(10, 30)},
                {"department": "可持续发展中心", "count": random.randint(15, 35)},
                {"department": "跨界创新孵化器", "count": random.randint(25, 60)}
            ]
        }
        
        updates = [
            {
                "date": "2023-05-15",
                "title": "突破性AI模型发布",
                "content": "我们的最新AI模型在理解人类情感方面取得重大突破，为人机交互开辟新纪元！该模型不仅能准确识别复杂的情感状态，还能生成富有同理心的回应，为未来的智能助手和心理健康应用铺平道路。",
                "link": "https://example.com/ai-breakthrough",
                "image": "https://path.to/ai_model_image.jpg"
            },
            {
                "date": "2023-05-01",
                "title": "全球创新马拉松",
                "content": "我们成功举办了一场48小时不间断的全球创新马拉松，来自50个国家的参与者共同探索未来城市解决方案。这次活动不仅产生了多个潜在的突破性项目，还建立了一个跨国界的创新者网络，为未来的合作奠定基础。",
                "link": "https://example.com/innovation-marathon",
                "image": "https://path.to/marathon_image.jpg"
            },
            {
                "date": "2023-04-20",
                "title": "量子计算突破",
                "content": "我们的量子计算团队成功实现了100量子比特的纠缠态，这一突破为解决复杂的优化问题和模拟分子结构开辟了新的可能性。这项技术有望在新材料开发、药物设计等领域带来革命性变革。",
                "link": "https://example.com/quantum-breakthrough",
                "image": "https://path.to/quantum_image.jpg"
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
                    st.markdown(f"""
                    <div class='value-card' style='background-color: {value["color"]}'>
                        <div class='value-icon'>{value['icon']}</div>
                        <h3>{value.get('title', '')}</h3>
                        <p>{value.get('description', '')}</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.write("核心价值观暂未提供")
        
        # 创新指数
        st.header("创新指数")
        innovation_index = random.randint(80, 100)
        
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = innovation_index,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "创新指数", 'font': {'size': 24}},
            delta = {'reference': 80, 'increasing': {'color': "RebeccaPurple"}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "darkblue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 50], 'color': 'cyan'},
                    {'range': [50, 80], 'color': 'royalblue'},
                    {'range': [80, 100], 'color': 'rebeccapurple'}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        
        st.plotly_chart(fig, use_container_width=True)
        
        # 最新动态
        st.header("突破性进展")
        if updates:
            for update in updates:
                with st.expander(f"{update.get('date', '')} - {update.get('title', '')}"):
                    cols = st.columns([2, 1])
                    with cols[0]:
                        st.markdown(f"<p class='update-content'>{update.get('content', '')}</p>", unsafe_allow_html=True)
                        if update.get("link"):
                            st.markdown(f"<a href='{update['link']}' target='_blank' class='learn-more-btn'>深入探索</a>", unsafe_allow_html=True)
                    with cols[1]:
                        st.image(update.get('image', 'https://via.placeholder.com/300x200'), use_column_width=True)
        else:
            st.write("暂无最新动态")
        
        # 互动环节
        st.header("参与创新")
        user_idea = st.text_area("分享你的创新想法：")
        if st.button("提交想法"):
            with st.spinner('正在处理你的创意...'):
                time.sleep(2)  # 模拟处理时间
            st.success("感谢你的贡献！我们的创新团队将认真评估你的想法。")
            st.balloons()
        
        # 快速链接
        st.header("探索更多")
        col1, col2, col3, col4, col5 = st.columns(5)
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
        with col5:
            if st.button("🤝 全球合作"):
                st.session_state.page = "global_collaboration"
        
        # 团队成员统计
        st.header("创新生态系统")
        members = team_data.get("members", [])
        total_members = sum(member['count'] for member in members)
        departments = [member['department'] for member in members]
        member_counts = [member['count'] for member in members]
        
        fig = go.Figure(data=[go.Pie(labels=departments, values=member_counts, hole=.3)])
        fig.update_layout(title_text="团队组成")
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("创新先锋", total_members, f"+{random.randint(5, 20)}")
        col2.metric("跨界部门", len(departments), "+2")
        col3.metric("全球合作伙伴", random.randint(50, 100), f"+{random.randint(3, 10)}")
        
    except Exception as e:
        st.error(f"创新过程中遇到了一些挑战: {str(e)}")
        st.write("别担心，这正是我们突破自我的机会！")

    # 添加CSS样式
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        
        body {
            font-family: 'Roboto', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: #333;
        }
        
        .welcome-section {
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            color: white;
            padding: 3rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            position: relative;
            overflow: hidden;
        }
        
        .welcome-section::before {
            content: "";
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: repeating-linear-gradient(
                0deg,
                transparent,
                transparent 20px,
                rgba(255, 255, 255, 0.1) 20px,
                rgba(255, 255, 255, 0.1) 40px
            );
            animation: move-background 10s linear infinite;
        }
        
        @keyframes move-background {
            0% {
                transform: rotate(0deg);
            }
            100% {
                transform: rotate(360deg);
            }
        }
        
        .welcome-section h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            position: relative;
        }
        
        .subtitle {
            font-size: 1.5rem;
            opacity: 0.9;
            margin-top: 1rem;
        }
        
        .scroll-down {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 30px;
            height: 50px;
            border: 2px solid #fff;
            border-radius: 25px;
        }
        
        .scroll-down::before {
            content: '';
            position: absolute;
            top: 10px;
            left: 50%;
            width: 6px;
            height: 6px;
            margin-left: -3px;
            background-color: #fff;
            border-radius: 100%;
            animation: scroll-down 2s infinite;
        }
        
        @keyframes scroll-down {
            0% {
                transform: translate(0, 0);
                opacity: 0;
            }
            40% {
                opacity: 1;
            }
            80% {
                transform: translate(0, 20px);
                opacity: 0;
            }
            100% {
                opacity: 0;
            }
        }
        
        .team-description {
            font-size: 1.3rem;
            line-height: 1.7;
            color: #333;
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            backdrop-filter: blur(5px);
        }
        
        .value-card {
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        
        .value-card:hover {
            transform: translateY(-10px) scale(1.05);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }
        
        .value-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .value-card h3 {
            color: #fff;
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }
        
        .value-card p {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1rem;
        }
        
        .update-content {
            font-size: 1.1rem;
            line-height: 1.6;
            color: #333;
        }
        
        .learn-more-btn {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 25px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 30px;
            transition: all 0.3s ease;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .learn-more-btn:hover {
            background-color: #45a049;
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
        }
        
        .stButton>button {
            width: 100%;
            border-radius: 30px;
            font-weight: bold;
            transition: all 0.3s ease;
            background-color: #3498db;
            color: white;
            text-transform: uppercase;
            letter-spacing: 1px;
            border: none;
            padding: 10px 15px;
        }
        
        .stButton>button:hover {
            transform: scale(1.05);
            background-color: #2980b9;
            box-shadow: 0 5px 15px rgba(52, 152, 219, 0.4);
        }
        
        .innovation-index {
            font-size: 2rem;
            font-weight: bold;
            color: #3498db;
            text-align: center;
            margin-top: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        /* 添加响应式设计 */
        @media (max-width: 768px) {
            .welcome-section h1 {
                font-size: 2.5rem;
            }
            
            .subtitle {
                font-size: 1.2rem;
            }
            
            .value-card {
                margin-bottom: 1rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    render_home()
