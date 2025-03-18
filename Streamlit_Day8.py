import streamlit as st
import pandas as pd

if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("Increment"):
    st.session_state.count += 1
st.write(f"Count: {st.session_state.count}")

## Assignment
if st.button("Reset"):
    st.session_state.count = 0
# Initialize session state for data persistence
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['ID', 'Player', 'IPL Team', 'Formats'])

st.title("Cricket Players database")
st.header("Only place to get all player info")

name = st.text_input("Enter player name")
ipl_team = st.selectbox("IPL franchise of the player", ["CSK", "DC", "GT", "KKR", "LSG", "MI", "PBKS", "RCB", "RR", "SRH"])
format_played = st.multiselect("Currently playing national team in format", ["Test", "ODI", "T20I"])

if st.button("Submit"):
    new_entry = pd.DataFrame({
        'ID': [ st.session_state.count ],
        'Player': [name],
        'IPL Team': [ipl_team],
        'Formats': [format_played]
    })

    st.session_state.df = pd.concat([st.session_state.df, new_entry], ignore_index=True)

st.table(st.session_state.df)
st.session_state.df.to_csv("players_data_live.csv")



