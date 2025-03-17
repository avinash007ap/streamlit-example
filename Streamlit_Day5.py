import streamlit as st
import pandas as pd
import json

df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
st.dataframe(df)


## Assignment
csv_file = "E:\\Learn\\RealPython\\RealPython_Courses\\PRACTICE\\CSV\\employee_birthday.csv"

with open(csv_file, "r") as file:
    data = file.read()
    

df2 = pd.read_csv(csv_file)

st.write("CSV file as a dataframe")
st.dataframe(df2)
st.divider()
st.write("CSV file as a table")
st.table(df2)
st.divider()
#json_data = json.dump(csv_file)
json_data = df2.to_json(orient="records", indent=4)

st.write("csv file as a json")
st.json(json_data)