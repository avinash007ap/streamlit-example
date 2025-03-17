import streamlit as st
password = st.text_input("Enter password:", type="password")
if password == "admin":
    st.write("Access granted!")
## Assignment
else:
    st.write("Incorrect password, Retry!")