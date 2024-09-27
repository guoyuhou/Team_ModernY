import streamlit as st
import json
from utils.db_utils import get_team_info
from utils.cache_utils import cache_data

@cache_data(ttl=3600)
def load_team_data():
    return get_team_info()

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
