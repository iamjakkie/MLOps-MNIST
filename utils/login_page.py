import streamlit as st
from utils.dashboard_page import run_dashboard_page

def run_login_page():
    st.subheader("Login page")

    login = st.text_input("Login")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if True:
            st.success("Successfully logged in!")
            return login