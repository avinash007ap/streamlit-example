import streamlit as st
import pandas as pd
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.image(uploaded_file)

### Assignment

upload = st.file_uploader("Choose a valid CSV file")
if upload:
    df = pd.read_csv(upload)
    st.table(df)
    download_data = df.to_csv()
    download = st.download_button(label="Download CSV", data=download_data, file_name="downloaded_player_data.csv")