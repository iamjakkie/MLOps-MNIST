import numpy as np 
import streamlit as st
import io 
from utils.login_page import run_login_page
from utils.dashboard_page import run_dashboard_page

def main():
    # Streamlit
    st.title("Simple MNIST example")

    menu = ['Login', 'Dashboard']
    choice = st.sidebar.selectbox("Menu", menu)
    login = None
    if choice == "Login":
        st.subheader("Login")
        login = run_login_page()
    elif choice == "Dashboard":
        st.subheader("Dashboard")
        run_dashboard_page(login)
    
if __name__ == "__main__":
    main()
        