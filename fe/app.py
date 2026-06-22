import streamlit as st

st.title("JOB Portal")

if st.button("Register"):
    st.switch_page("pages/register.py")

if st.button("Login"):
    st.switch_page("pages/login.py")