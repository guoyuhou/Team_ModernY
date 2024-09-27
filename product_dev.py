import streamlit as st

def render_product_dev():
    st.title("产品开发流程")
    
    dev_process = [
        {
            "name": "需求分析",
            "description": "收集和分析用户需求",
            "steps": [
                {
                    "title": "用户调研",
                    "content": "通过问卷、访谈等方式收集用户反馈",
                    "tools": ["问卷星", "用户访谈记录表"]
                },
                {
                    "title": "需求文档编写",
                    "content": "整理用户需求，编写需求规格说明书",
                    "tools": ["Confluence", "JIRA"]
                }
            ]
        },
        {
            "name": "设计阶段",
            "description": "进行产品原型和UI设计",
            "steps": [
                {
                    "title": "原型设计",
                    "content": "创建低保真和高保真原型",
                    "tools": ["Axure", "Figma"]
                },
                {
                    "title": "UI设计",
                    "content": "设计用户界面和视觉风格",
                    "tools": ["Sketch", "Adobe XD"]
                }
            ]
        },
        {
            "name": "开发阶段",
            "description": "进行产品的实际开发工作",
            "steps": [
                {
                    "title": "代码编写",
                    "content": "根据设计文档进行编码",
                    "tools": ["Visual Studio Code", "Git"]
                },
                {
                    "title": "代码审查",
                    "content": "进行代码质量检查和优化",
                    "tools": ["GitHub", "GitLab"]
                }
            ]
        },
        {
            "name": "测试阶段",
            "description": "进行产品质量测试",
            "steps": [
                {
                    "title": "单元测试",
                    "content": "对各个模块进行单独测试",
                    "tools": ["JUnit", "PyTest"]
                },
                {
                    "title": "集成测试",
                    "content": "测试各模块之间的交互",
                    "tools": ["Selenium", "Postman"]
                }
            ]
        },
        {
            "name": "发布阶段",
            "description": "产品正式发布和上线",
            "steps": [
                {
                    "title": "部署",
                    "content": "将产品部署到生产环境",
                    "tools": ["Docker", "Kubernetes"]
                },
                {
                    "title": "监控",
                    "content": "监控产品运行状况",
                    "tools": ["Prometheus", "Grafana"]
                }
            ]
        }
    ]
    
    for stage in dev_process:
        st.header(stage["name"])
        st.write(stage["description"])
        
        for step in stage["steps"]:
            st.subheader(step["title"])
            st.write(step["content"])
            
            if "tools" in step:
                st.write("推荐工具:")
                for tool in step["tools"]:
                    st.write(f"- {tool}")
        
        st.write("---")
    
    st.button("开始新项目", on_click=start_new_project)

def start_new_project():
    # 实现开始新项目的逻辑
    st.success("新项目已创建!")

__all__ = ['render_product_dev']

if __name__ == "__main__":
    render_product_dev()
