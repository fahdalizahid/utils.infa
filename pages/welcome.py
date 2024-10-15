import streamlit as st
import navigation

#------------------------------DEFINITIONS---------------------

    
#------------------------------TOP SECTION---------------------


st.image("resources/home_repair_service_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg", width=200)
st.title("Infa Utils")
st.write("Master your ETL jobs")



# --- ACTIONS ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.subheader("Create", anchor=False)
    st.write("Create a new project")
    if st.button("Create"):
        st.switch_page(navigation.new_project)

with col2:
    st.subheader("Open", anchor=False)
    st.write("Open an existing project")
    