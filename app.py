import streamlit as st
from db_C import cursor,con
from dashboard import dashboard

st.title("Media Platform")


# If user click on Sign-Up Button
def signUp():
    st.subheader("Sign-Up")
    with st.form("Sign-UP_Form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password",type="password")
        Signup_btt=st.form_submit_button("Sign-Up")

        if Signup_btt:
            query = "insert into users(name,email,password) values(%s,%s,%s)"
            values = (name,email,password)
            cursor.execute(query,values)
            con.commit()

            st.success("User data Registered")


# If user click on Login Button
def login():
    st.subheader("Login")
    with st.form("Login_Form"):
        email = st.text_input("Email")
        password = st.text_input("Password",type="password")
        Login_btt =st.form_submit_button("Login")

        if Login_btt:
            query = "select * from users where email = %s and password = %s "
            values = (email,password)
            cursor.execute(query,values)

            logined_user = cursor.fetchone()
            
            if logined_user:
                st.session_state.user=logined_user
                st.success("Login Successfully")
                st.rerun()
            else:
                st.error("Invalid Email or Password")


if st.session_state.user == None:       #if session is None then it should display the signup and login tabs
    login_tab,signUp_tab = st.tabs(
    ["Login","SignUp"]    
    )
    with signUp_tab:
        signUp()
    with login_tab:
        login()

else:                         #if not it should display the dashboard
    dashboard()

        
        

  


