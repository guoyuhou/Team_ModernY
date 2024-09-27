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
    
    st.header("团队愿景")
    st.write(team_data["vision"])
    
    st.header("团队文化")
    for value in team_data["culture"]:
        st.subheader(value["title"])
        st.write(value["description"])
    
    st.header("团队成员")
    cols = st.columns(3)
    for idx, member in enumerate(team_data["members"]):
        with cols[idx % 3]:
            st.image(member["avatar"], width=150)
            st.subheader(member["name"])
            st.write(member["position"])
            st.write(member["bio"])

__all__ = ['render_team_info']

if __name__ == "__main__":
    render_team_info()
