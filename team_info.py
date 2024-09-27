import streamlit as st

def load_team_data():
    return {
        "vision": "成为行业领先的创新型科技公司",
        "culture": [
            {"title": "创新", "description": "我们鼓励创新思维和解决问题的新方法"},
            {"title": "团队合作", "description": "我们相信通过协作可以实现更大的目标"},
            {"title": "客户至上", "description": "我们始终将客户的需求放在首位"}
        ],
        "members": [
            {
                "name": "张三",
                "position": "CEO",
                "bio": "拥有10年科技行业经验",
                "avatar": "https://example.com/zhangsan.jpg"
            },
            {
                "name": "李四",
                "position": "CTO",
                "bio": "专注于人工智能和机器学习",
                "avatar": "https://example.com/lisi.jpg"
            },
            {
                "name": "王五",
                "position": "产品经理",
                "bio": "擅长用户体验设计",
                "avatar": "https://example.com/wangwu.jpg"
            }
        ]
    }

def render_team_info():
    st.title("团队信息")
    
    team_data = load_team_data()
    
    st.markdown(
        """
        <div class="team-vision">
            <h2>团队愿景</h2>
            <p class="vision-text">成为行业领先的创新型科技公司</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h2>团队文化</h2>", unsafe_allow_html=True)
    for value in team_data["culture"]:
        st.markdown(
            f"""
            <div class="culture-item">
                <h3>{value["title"]}</h3>
                <p>{value["description"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("<h2>团队成员</h2>", unsafe_allow_html=True)
    for member in team_data["members"]:
        st.markdown(
            f"""
            <div class="team-member">
                <img src="{member['avatar']}" alt="{member['name']}">
                <h3>{member['name']}</h3>
                <p class="position">{member['position']}</p>
                <p class="bio">{member['bio']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 添加CSS和JavaScript
    st.markdown(
        """
        <style>
        .team-vision {
            background-color: #f0f2f6;
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 2rem;
        }
        .vision-text {
            font-size: 1.5rem;
            font-weight: bold;
            color: #262730;
        }
        .culture-item {
            background-color: white;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            transition: transform 0.3s;
        }
        .culture-item:hover {
            transform: translateY(-5px);
        }
        .team-member {
            background-color: white;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            text-align: center;
        }
        .team-member img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 1rem;
        }
        .team-member .position {
            font-style: italic;
            color: #666;
        }
        </style>
        <script>
        // 添加简单的滚动动画
        document.addEventListener('DOMContentLoaded', (event) => {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = 1;
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            });

            document.querySelectorAll('.culture-item, .team-member').forEach((el) => {
                el.style.opacity = 0;
                el.style.transform = 'translateY(20px)';
                el.style.transition = 'opacity 0.5s, transform 0.5s';
                observer.observe(el);
            });
        });
        </script>
        """,
        unsafe_allow_html=True
    )

__all__ = ['render_team_info']

if __name__ == "__main__":
    render_team_info()
