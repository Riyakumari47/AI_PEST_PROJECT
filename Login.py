import streamlit as st

st.title("🔐 User Login")
st.write("Please enter your credentials to access the system.")

username = st.text_input("Username / Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username and password:
        st.success(f"🎉 Welcome, {username}! Login Successful. Please go to the 'Detection' page from the sidebar.")
    else:
        st.warning("⚠️ Please enter any Username and Password to proceed.")