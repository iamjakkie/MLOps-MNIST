import streamlit as st
from utils.dashboard_page import run_dashboard_page
from utils.aws_utils import auth

def hash_password(password:str) -> str:
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password:str, provided_password:str) -> bool:
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def run_login_page():
    st.subheader("Login page")

    login = st.text_input("Login")
    password = has_password(st.text_input("Password", type='password'))

    if st.button("Login"):
        if auth(login, password):
            st.success("Successfully logged in!")
            return login