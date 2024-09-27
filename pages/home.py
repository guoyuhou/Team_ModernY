import streamlit as st
from utils.db_utils import get_team_info, get_latest_updates
from utils.cache_utils import cache_data

@cache_data(ttl=3600)
def load_team_data():
    return get_team_info()

@cache_data(ttl=300)
def load_latest_updates():
    return get_latest_updates()

def render_home():
    st.title("欢迎来到我们的团队内部平台")
    
    try:
        # 加载团队信息
        team_data = load_team_data()
        
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
        updates = load_latest_updates()
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
        st.write("请检查数据库连接和数据格式是否正确。")

__all__ = ['render_home']

if __name__ == "__main__":
    render_home()
