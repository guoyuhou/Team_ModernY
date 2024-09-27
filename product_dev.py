import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_product_dev():
    st.title("创新产品开发之旅")
    
    # 添加动画效果
    lottie_url = "https://assets3.lottiefiles.com/packages/lf20_jtbfg2nb.json"
    lottie_json = load_lottie_url(lottie_url)
    st_lottie(lottie_json, speed=1, height=200, key="product_dev_animation")

    dev_process = [
        {
            "name": "灵感迸发",
            "description": "捕捉创意火花，洞察用户需求",
            "icon": "lightbulb",
            "color": "#FFD700",
            "steps": [
                {
                    "title": "创意风暴",
                    "content": "组织头脑风暴会议，激发团队创意",
                    "tools": ["思维导图", "创意白板"]
                },
                {
                    "title": "用户洞察",
                    "content": "深入用户群体，发现潜在需求",
                    "tools": ["用户画像", "同理心地图"]
                }
            ]
        },
        {
            "name": "概念设计",
            "description": "将创意转化为可视化概念",
            "icon": "pencil-alt",
            "color": "#4CAF50",
            "steps": [
                {
                    "title": "原型魔法",
                    "content": "快速创建交互原型，验证设计理念",
                    "tools": ["Figma", "Adobe XD"]
                },
                {
                    "title": "视觉盛宴",
                    "content": "打造令人惊艳的用户界面",
                    "tools": ["Sketch", "Illustrator"]
                }
            ]
        },
        {
            "name": "技术锻造",
            "description": "将创意付诸实践，构建产品骨架",
            "icon": "code",
            "color": "#2196F3",
            "steps": [
                {
                    "title": "代码编织",
                    "content": "将设计蓝图转化为功能代码",
                    "tools": ["VS Code", "GitHub"]
                },
                {
                    "title": "质量炼金",
                    "content": "通过代码审查提升产品品质",
                    "tools": ["SonarQube", "CodeClimate"]
                }
            ]
        },
        {
            "name": "品质淬炼",
            "description": "全方位测试，打造完美体验",
            "icon": "vial",
            "color": "#9C27B0",
            "steps": [
                {
                    "title": "功能探索",
                    "content": "全面测试各个功能模块",
                    "tools": ["Selenium", "Cypress"]
                },
                {
                    "title": "用户体验优化",
                    "content": "收集反馈，不断改进产品体验",
                    "tools": ["UserTesting", "Hotjar"]
                }
            ]
        },
        {
            "name": "闪耀登场",
            "description": "产品华丽亮相，开启市场征程",
            "icon": "rocket",
            "color": "#FF5722",
            "steps": [
                {
                    "title": "云端部署",
                    "content": "将产品安全部署到云端环境",
                    "tools": ["Docker", "Kubernetes"]
                },
                {
                    "title": "数据守护",
                    "content": "实时监控产品运行状态",
                    "tools": ["Grafana", "Datadog"]
                }
            ]
        }
    ]
    
    for stage in dev_process:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f'<i class="fas fa-{stage["icon"]} fa-3x" style="color: {stage["color"]};"></i>', unsafe_allow_html=True)
            with col2:
                st.subheader(stage["name"])
                st.write(stage["description"])
        
        for step in stage["steps"]:
            with st.expander(step["title"]):
                st.write(step["content"])
                
                if "tools" in step:
                    st.write("创新工具箱:")
                    for tool in step["tools"]:
                        st.markdown(f'<span class="tool-badge">{tool}</span>', unsafe_allow_html=True)
        
        st.markdown('<hr class="stage-divider">', unsafe_allow_html=True)
    
    if st.button("启动创新项目", key="start_project"):
        st.balloons()
        st.success("恭喜你！新的创新项目已经启动，让我们一起开启这段激动人心的旅程吧！")

    # 添加CSS样式
    st.markdown(
        """
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');
        .stExpander {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 20px;
            margin-bottom: 20px;
            box-shadow: 5px 5px 15px #d1d1d1, -5px -5px 15px #ffffff;
            transition: all 0.3s ease;
        }
        .stExpander:hover {
            transform: translateY(-5px);
            box-shadow: 8px 8px 20px #d1d1d1, -8px -8px 20px #ffffff;
        }
        .stExpander > div:first-child {
            border-bottom: 2px solid #e0e0e0;
            padding: 15px;
            font-weight: bold;
            color: #333;
        }
        .stButton>button {
            width: 100%;
            border-radius: 30px;
            font-weight: bold;
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            color: white;
            border: none;
            padding: 15px 0;
            font-size: 18px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        .tool-badge {
            display: inline-block;
            background-color: #e0e0e0;
            color: #333;
            padding: 5px 10px;
            border-radius: 15px;
            margin: 5px;
            font-size: 0.9em;
        }
        .stage-divider {
            border: 0;
            height: 1px;
            background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0));
            margin: 30px 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    render_product_dev()
