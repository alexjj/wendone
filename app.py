import streamlit as st
import datetime

target_datetime = datetime.datetime(2025, 2, 20, 13, 00, 0)
current_datetime = datetime.datetime.now()

if current_datetime < target_datetime:
    st.image("notdone.png", caption="Not yet!")
else:
    st.image("done.png", caption="It's time!")
    st.balloons()
