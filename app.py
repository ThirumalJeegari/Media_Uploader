import streamlit as st

st.title("Media Platform")

login,signUp = st.tabs(
    ["Login","SignUp"]    
)

with signUp:
    st.subheader("Sign-Up")
    with st.form("Sign-UP_Form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password",type="password")
        bt=st.form_submit_button("Sign-Up")

with login:
    st.subheader("Login")
    with st.form("Login_Form"):
        name = st.text_input("Name")
        password = st.text_input("Password",type="password")
        bt=st.form_submit_button("Login")
