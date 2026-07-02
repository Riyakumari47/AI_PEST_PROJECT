import streamlit as st

st.title("📊 Detection History")

if "history" not in st.session_state:
    st.session_state["history"] = []

for item in st.session_state["history"]:
    st.write(item)