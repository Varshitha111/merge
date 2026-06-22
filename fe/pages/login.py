import streamlit as st
import requests

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

    try:
        res = requests.post(
            f"{b_url}/login",
            json=payload
        )

        st.write("Status Code:", res.status_code)

        if res.status_code != 200:
            st.error("Backend Error")
            st.write(res.text)
            st.stop()

        response_data = res.json()

        st.write("Response:", response_data)

        data = response_data["obj_supabase"]["data"]

        if len(data) == 0:
            st.error("Invalid Credentials")
        else:
            user = data[0]

            # Save user in session
            st.session_state["logged_user"] = user

            st.success("Login Successful")

            if user["role"] == "recruiter":
                st.switch_page("pages/recruiter_dashboard.py")
            else:
                st.switch_page("pages/job_seeker_dashboard.py")

    except Exception as e:
        st.error(f"Error: {e}")
