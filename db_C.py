import mysql.connector
import streamlit as st

con = mysql.connector.connect(
    host = st.secrets["host"],
    user = st.secrets["user"],
    password = st.secrets["password"],
    database = st.secrets["database"],
    port = st.secrets["port"],
    auth_plugin="mysql_native_password"
)

cursor = con.cursor(dictionary=True)

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS files(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    file_name VARCHAR(255),
    file_type VARCHAR(100),
    file_url TEXT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

con.commit()



