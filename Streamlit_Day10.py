import streamlit as st
import requests
response = requests.get("https://api.github.com")
st.json(response.json())
