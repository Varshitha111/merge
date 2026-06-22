import requests
import streamlit as st
# pip install streamlit-local-storage
from streamlit_local_storage import LocalStorage

ls=LocalStorage()



b_url = st.secrets["b_url"]
st.subheader("Login Form")

with st.form("LoginForm"):
    e = st.text_input("Email")
    p = st.text_input("Password", type="password")
    r = st.selectbox(
        "Choose Role:",
        ["recruiter", "job_seeker"]
    )

    l_sub_btn = st.form_submit_button("Login")

if l_sub_btn:
    payload = {
        "email": e,
        "password": p,
        "role": r
    }

    res = requests.post(
        f"{b_url}/login",
        json=payload
    )

    data = res.json()["obj_supabase"]["data"]

    if len(data) == 0:
        st.error("User not found")
    else:
        st.success("Login Success")
        st.write(data)
        user=data[0] #{}
        st.session_state["logged_user"] = user
        if data[0]["role"]=="recruiter":
            st.switch_page("pages/recruiter_dashboard.py")
        else:
            st.switch_page("pages/job_seeker_dashboard.py")
            
        # Example:
        # st.session_state["logged_user"] = data[0]
        # st.switch_page("pages/recruiter_dashboard.py")