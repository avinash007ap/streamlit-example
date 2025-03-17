import streamlit as st
color = st.selectbox("Pick a color", ["Red", "Green", "Blue"])
st.write(f"You selected: {color}")

## Assignment
ball = st.radio("Select your preferred color of cricket ball", ["Red", "White"])
runs = st.slider("How many runs will be scored today", 0, 400)
wickets = st.slider("How many wickets will fall today", 0, 20)
watch_live = st.checkbox("Are you ready to watch match live", True)
formats = st.multiselect("Select your favorite formats/leagues", ["Test", "ODI", "T20I", "T20", "T10", "Hundred", "IPL", "BBL"], ["T20I", "IPL"])

if watch_live:
    watch = "Yes! Bring it ONN"
else:
    watch = "Maybe Next Time."

st.write(f"""Welcome, cricket fan! As you love {ball} game & expect {runs} scored, {wickets} fallen.
        Here's how you cna watch the game as per your interest {watch}, 
        Enjoy {formats} and more in our app! Download now!!""")
