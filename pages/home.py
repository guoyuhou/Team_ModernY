import streamlit as st
from utils.db_utils import get_team_info, get_latest_updates
from utils.cache_utils import cache_data

@cache_data(ttl=3600)
def load_team_data():
    return get_team_info()

@cache_data(ttl=300)
def load_latest_updates():
    return get_latest_updates()

def render():
    st.title("欢迎来到我们的团队内部平台")
    
    # 加载团队信息
    team_data = load_team_data()
    
    # 团队简介
    st.header("关于我们")
    st.write(team_data["description"])
    
    # 团队愿景
    st.subheader("我们的愿景")
    st.info(team_data["vision"])
    
    # 核心价值观
    st.subheader("核心价值观")
    cols = st.columns(len(team_data["values"]))
    for idx, value in enumerate(team_data["values"]):
        with cols[idx]:
            st.metric(label=value["title"], value=value["description"])
    
    # 最新动态
    st.header("最新动态")
    updates = load_latest_updates()
    for update in updates:
        with st.expander(f"{update['date']} - {update['title']}"):
            st.write(update["content"])
            if update.get("link"):
                st.markdown(f"[了解更多]({update['link']})")
    
    # 快速链接
    st.header("快速链接")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("查看团队信息", on_click=lambda: setattr(st.session_state, 'page', 'team_info'))
    with col2:
        st.button("浏览产品开发流程", on_click=lambda: setattr(st.session_state, 'page', 'product_dev'))
    with col3:
        st.button("访问学习资源", on_click=lambda: setattr(st.session_state, 'page', 'learning_resources'))
    
    # 团队成员统计
    st.header("团队概况")
    total_members = len(team_data["members"])
    departments = set(member["department"] for member in team_data["members"])
    
    col1, col2 = st.columns(2)
    col1.metric("团队成员总数", total_members)
    col2.metric("部门数量", len(departments))
    
    # 团队氛围图片
    team_spirit_image_url = "https://img.freepik.com/free-photo/group-diverse-people-having-business-meeting_53876-25060.jpg"
    st.image(team_spirit_image_url, caption="我们的团队氛围", use_column_width=True)

if __name__ == "__main__":
    render()
