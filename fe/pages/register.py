import streamlit as st
import requests 

b_url = st.secrets["b_url"]



st.subheader("RegisterForm")

with st.form("RegisterForm"):
    n=st.text_input("Name")
    p=st.text_input("Password",type="password")
    c_p=st.text_input("Confirm_Password",type="password")
    e=st.text_input("Email")
    r=st.selectbox("Choose Role :-- ",["recruiter","job_seeker"])

    r_sub_btn=st.form_submit_button("Register")


    if r_sub_btn:
        payload={
            "name":n,
            "password":p,
            "confirm_password":c_p,
            "email":e,
            "role":r
            }

        res=requests.post(f"{b_url}/register",json=payload)
        st.write(res.json())
        st.switch_page("pages/login.py")

if st.button("Login"):
    st.switch_page("pages/login.py")        
