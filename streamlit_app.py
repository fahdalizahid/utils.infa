import navigation as nav



#----------------------------------INIT_NAVIGATION--------------
 #------------------NAVIGATION SETUP---------------
pg = nav.st.navigation(
    {
        "📚 Projects":[nav.welcome_page,nav.new_project],
        " Open Projects":[],
        "⚙️ Configuration":[nav.repo_config_page],
    }
)
pg.run()

