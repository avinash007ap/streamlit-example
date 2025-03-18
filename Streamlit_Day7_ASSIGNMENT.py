import streamlit as st
import pandas as pd

CSV_FILE = "players_data.csv"

try:
    df = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=['ID', 'Player', 'IPL Team'])

# data = {
#     'ID': [],
#     'Player': [],
#     'IPL Team': []
# }
# df = pd.DataFrame(data)

st.title("Cricket Players database")
st.header("Only place to get all player info")

name = st.text_input("Enter player name")
ipl_team = st.selectbox("IPL franchise of the player", ["CSK", "DC", "GT", "KKR", "LSG", "MI", "PBKS", "RCB", "RR", "SRH"])

if st.button("Submit"):
    new_entry = pd.DataFrame({'ID': [len(df) + 1], 'Player': [name], 'IPL Team': [ipl_team]})
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)  # Save data to file

st.dataframe(df)

# if st.button("Submit"):
#     id = len(data['ID']) + 1
#     data['ID'].append(id)
#     data['Player'].append(name)
#     data['IPL Team'].append(ipl_team)
#     st.dataframe(data)