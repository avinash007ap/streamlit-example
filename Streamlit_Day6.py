import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(20, 2), columns=["X", "Y"])
st.line_chart(df)

st.title("HR Data of organization")

csv_file = "E:\\Learn\\RealPython\\RealPython_Courses\\PRACTICE\\CSV\\hrdata.csv"

# with open(csv_file, "r") as file:
#     data = file.read()
df2 = pd.read_csv(csv_file)
col1, col2 = st.columns(2)

with col1:
    st.header("Employees Salary: line")
    st.line_chart(df2, x="Name", y=["Salary"])
    st.divider()
    st.header("Employees Salary: bar")
    st.bar_chart(df2, x="Name", y=["Salary"])
    st.divider()

with col2:
    st.header("Employees Sick days: line")
    st.line_chart(df2, x="Name", y=["Sick Days remaining"])
    st.divider()
    st.header("Employees Sick days: bars")
    st.bar_chart(df2, x="Name", y=["Sick Days remaining"])
    st.divider()

# st.write("HR Data: pyplot")
# st.pyplot(df2)
