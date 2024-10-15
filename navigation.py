import streamlit as st

#------------------PAGE SETUP---------------
#WELCOME
welcome_page = st.Page(
    page="pages/welcome.py",
    title="Welcome",
    icon=":material/home_repair_service:",
    default=True,
    
)
#NEW_PROJECT
new_project = st.Page(
    page="pages/new_project.py",
    title="Create New Project",
    icon=":material/add_ad:", 
    
)
#CONFIG
repo_config_page = st.Page(
    page="pages/repo_config.py",
    title="Repo Config",
    icon=":material/deployed_code:",
    
)
