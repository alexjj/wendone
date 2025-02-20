import streamlit as st
import datetime

target_datetime = datetime.datetime(2025, 2, 20, 13, 00, 0)
current_datetime = datetime.datetime.now()

st.set_page_config(layout='centered', page_title="wen done", page_icon=":older_man:")

if current_datetime < target_datetime:
    st.image("notdone.png", caption="Not yet!")
else:
    st.image("done.png", caption="It's time!")
    st.balloons()
