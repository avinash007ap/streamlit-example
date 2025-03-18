import streamlit as st
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}!")

## Assignment
age = st.number_input("Enter your age:")
feedback = st.text_area("Your feedback here:")
if st.button("Create"):
    st.write(f"Thanks for your feedback, {name}")