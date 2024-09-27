import streamlit as st

def load_team_data():
    return {
        "vision": "成为行业领先的创新型科技公司",
        "culture": [
            {"title": "创新", "description": "我们鼓励创新思维和解决问题的新方法", "icon": "🚀"},
            {"title": "团队合作", "description": "我们相信通过协作可以实现更大的目标", "icon": "🤝"},
            {"title": "客户至上", "description": "我们始终将客户的需求放在首位", "icon": "👑"}
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
            <h2 class="vision-title">团队愿景</h2>
            <p class="vision-text">{}</p>
        </div>
        """.format(team_data["vision"]),
        unsafe_allow_html=True
    )
    
    st.markdown("<h2 class='section-title'>团队文化</h2>", unsafe_allow_html=True)
    for value in team_data["culture"]:
        st.markdown(
            f"""
            <div class="culture-item">
                <div class="culture-icon">{value["icon"]}</div>
                <h3>{value["title"]}</h3>
                <p>{value["description"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("<h2 class='section-title'>团队成员</h2>", unsafe_allow_html=True)
    for member in team_data["members"]:
        st.markdown(
            f"""
            <div class="team-member">
                <div class="member-avatar" style="background-image: url('{member['avatar']}')"></div>
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
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }

        .team-vision {
            background: linear-gradient(45deg, #3498db, #2980b9);
            padding: 3rem;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 3rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transform: perspective(1000px) rotateX(5deg);
            transition: transform 0.3s ease-in-out;
        }

        .team-vision:hover {
            transform: perspective(1000px) rotateX(0deg);
        }

        .vision-title {
            color: #fff;
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }

        .vision-text {
            font-size: 1.8rem;
            font-weight: bold;
            color: #ecf0f1;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }

        .section-title {
            text-align: center;
            font-size: 2.5rem;
            color: #2c3e50;
            margin-bottom: 2rem;
            position: relative;
        }

        .section-title::after {
            content: '';
            display: block;
            width: 50px;
            height: 3px;
            background: #3498db;
            margin: 10px auto;
        }

        .culture-item {
            background-color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            margin-bottom: 2rem;
            transition: all 0.3s ease;
            text-align: center;
        }

        .culture-item:hover {
            transform: translateY(-10px) scale(1.03);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }

        .culture-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .team-member {
            background-color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            margin-bottom: 2rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .team-member:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }

        .member-avatar {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            background-size: cover;
            background-position: center;
            margin: 0 auto 1.5rem;
            border: 5px solid #3498db;
            transition: all 0.3s ease;
        }

        .team-member:hover .member-avatar {
            transform: scale(1.1) rotate(5deg);
        }

        .team-member h3 {
            color: #2c3e50;
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
        }

        .team-member .position {
            font-style: italic;
            color: #7f8c8d;
            margin-bottom: 1rem;
        }

        .team-member .bio {
            color: #34495e;
            font-size: 1rem;
            line-height: 1.6;
        }
        </style>
        <script>
        document.addEventListener('DOMContentLoaded', (event) => {
            // 添加滚动动画
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('animate');
                    }
                });
            }, {threshold: 0.1});

            document.querySelectorAll('.culture-item, .team-member').forEach((el) => {
                el.style.opacity = '0';
                el.style.transform = 'translateY(50px)';
                el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                observer.observe(el);
            });

            // 添加动画类
            document.querySelectorAll('.animate').forEach((el) => {
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            });

            // 添加鼠标悬停效果
            document.querySelectorAll('.team-member').forEach((el) => {
                el.addEventListener('mousemove', (e) => {
                    const rect = el.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    el.style.setProperty('--mouse-x', `${x}px`);
                    el.style.setProperty('--mouse-y', `${y}px`);
                });
            });
        });
        </script>
        """,
        unsafe_allow_html=True
    )

__all__ = ['render_team_info']

if __name__ == "__main__":
    render_team_info()
