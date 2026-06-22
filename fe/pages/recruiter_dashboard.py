import streamlit as st
import requests as r

# Check Login
if "logged_user" not in st.session_state:
    st.error("Please login first")
    st.switch_page("pages/login.py")
    st.stop()

b_url = st.secrets["b_url"]

st.title("Recruiter Dashboard")

st.write(f"Welcome {st.session_state['logged_user']['name']}")

pic = st.file_uploader(
    "Choose Profile Picture",
    type=["png", "jpg", "jpeg"]
)

exp = st.number_input(
    "Experience (Years)",
    min_value=0,
    step=1
)

company = st.text_input("Company")

if st.button("Save Profile"):

    if pic is None:
        st.error("Please upload a profile picture")
    elif company.strip() == "":
        st.error("Please enter company name")
    else:

        payload = {
            "experience": int(exp),
            "company": company,
            "user_id": str(st.session_state["logged_user"]["id"])
        }

        files = {
            "pic": (
                pic.name,
                pic.getvalue(),
                pic.type
            )
        }

        try:
            res = r.post(
                f"{b_url}/profile_recruiter",
                data=payload,
                files=files
            )

            st.write("Status Code:", res.status_code)

            if res.status_code == 200:
                st.success("Profile Created Successfully")
                st.json(res.json())
            else:
                st.error("Backend Error")
                st.write(res.text)

        except Exception as e:
            st.error(f"Error: {e}")

st.divider()

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("pages/login.py")
