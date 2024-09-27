import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_home():
    # 加载动画
    lottie_welcome = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
    
    # 欢迎部分
    st.markdown(
        """
        <div class="welcome-section">
            <h1>欢迎来到我们的创新团队平台</h1>
            <p>在这里，我们激发灵感，培养创新，共同成长。</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 显示欢迎动画
    st_lottie(lottie_welcome, height=300, key="welcome")
    
    try:
        # 静态数据
        team_data = {
            "description": "我们是一群充满激情的创新者，致力于用技术改变世界。",
            "vision": "成为引领行业变革的技术先锋。",
            "values": [
                {"title": "创新", "description": "突破界限，创造未来", "icon": "🚀"},
                {"title": "协作", "description": "凝聚力量，共创辉煌", "icon": "🤝"},
                {"title": "诚信", "description": "诚实守信，赢得信赖", "icon": "🌟"}
            ],
            "members": [
                {"department": "技术部"},
                {"department": "创意设计部"},
                {"department": "市场营销部"},
                {"department": "客户体验部"},
                {"department": "数据分析部"}
            ]
        }
        
        updates = [
            {
                "date": "2023-05-01",
                "title": "革命性产品发布",
                "content": "我们的最新产品已成功上线，它将彻底改变用户的使用体验！",
                "link": "https://example.com/revolutionary-product"
            },
            {
                "date": "2023-04-15",
                "title": "创新工作坊",
                "content": "上周末，我们举办了一场激动人心的创新工作坊，激发了团队的创造力。",
                "link": None
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
        
        # 最新动态
        st.header("最新动态")
        if updates:
            for update in updates:
                with st.expander(f"{update.get('date', '')} - {update.get('title', '')}"):
                    st.markdown(f"<p class='update-content'>{update.get('content', '')}</p>", unsafe_allow_html=True)
                    if update.get("link"):
                        st.markdown(f"<a href='{update['link']}' target='_blank' class='learn-more-btn'>了解更多</a>", unsafe_allow_html=True)
        else:
            st.write("暂无最新动态")
        
        # 快速链接
        st.header("探索更多")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("👥 团队信息"):
                st.session_state.page = "team_info"
        with col2:
            if st.button("🔧 产品开发流程"):
                st.session_state.page = "product_dev"
        with col3:
            if st.button("📚 学习资源"):
                st.session_state.page = "learning_resources"
        
        # 团队成员统计
        st.header("团队概况")
        members = team_data.get("members", [])
        total_members = len(members)
        departments = set(member.get("department", "") for member in members)
        
        col1, col2 = st.columns(2)
        col1.metric("团队成员", total_members, "充满活力")
        col2.metric("创新部门", len(departments), "多元协作")
        
    except Exception as e:
        st.error(f"哎呀！似乎出了点小问题: {str(e)}")
        st.write("别担心，我们的技术精灵正在全力修复。")

    # 添加CSS样式
    st.markdown(
        """
        <style>
        .welcome-section {
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            text-align: center;
        }
        .welcome-section h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        .team-description {
            font-size: 1.2rem;
            line-height: 1.6;
            color: #4a4a4a;
        }
        .value-card {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        .value-card:hover {
            transform: translateY(-5px);
        }
        .update-content {
            font-size: 1rem;
            line-height: 1.5;
            color: #4a4a4a;
        }
        .learn-more-btn {
            display: inline-block;
            margin-top: 10px;
            padding: 5px 15px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 20px;
            transition: background-color 0.3s ease;
        }
        .learn-more-btn:hover {
            background-color: #45a049;
        }
        .stButton>button {
            width: 100%;
            border-radius: 20px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.05);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    render_home()
