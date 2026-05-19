import streamlit as st
from db_C import cursor,con

st.title("Media Platform")

login,signUp = st.tabs(
    ["Login","SignUp"]    
)



# If user click on Sign-Up Button
with signUp:
    st.subheader("Sign-Up")
    with st.form("Sign-UP_Form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password",type="password")
        Signup_btt=st.form_submit_button("Sign-Up")

        if Signup_btt:
            check_query = """
            SELECT * FROM users
            WHERE email=%s
            """

            cursor.execute(check_query, (email,))

            user = cursor.fetchone()


            if user:
                st.error("Email already exists")

            else:

                insert_query = """
                INSERT INTO users(name, email, password)
                VALUES(%s, %s, %s)
                """

                values = (name, email, password)

                cursor.execute(insert_query, values)

                con.commit()

                st.success("Account Created Successfully")



# If user click on Login Button
with login:
    st.subheader("Login")
    with st.form("Login_Form"):
        name = st.text_input("Name")
        password = st.text_input("Password",type="password")
        Login_btt =st.form_submit_button("Login")

        if Login_btt:

            login_query = """
            SELECT * FROM users
            WHERE email=%s AND password=%s
            """

            values = (email, password)

            cursor.execute(login_query, values)

            user = cursor.fetchone()

            if user:
                st.success(f"Welcome {user['name']}")

            else:
                st.error("Invalid Email or Password")

        

  


