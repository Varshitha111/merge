import streamlit as st
import requests as r

b_url = st.secrets["b_url"]



st.title("Recruiter Dashboard")

pic = st.file_uploader(
    "Choose Pic",
    type=["png", "jpg", "jpeg"]
)

exp = st.number_input("Experience")

company = st.text_input("Company")

if st.button("Save Profile"):

    payload = {
        "experience": exp,
        "company": company,
        "user_id": st.session_state["logged_user"]["id"]
    }

    res = r.post(
        f"{b_url}/profile_recruiter",
        data=payload,
        files={"pic": pic}
    )

    st.write(res.json())
