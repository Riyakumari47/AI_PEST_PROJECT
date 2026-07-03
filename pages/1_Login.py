import streamlit as st

st.set_page_config(page_title="Login", layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#0f172a,#111827);
    color: white;
}

.block-container {
    padding-top: 1rem !important;
}

.login-box {
    background: rgba(255,255,255,0.08);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
}

.stButton > button {
    background: #22c55e;
    color: black;
    width: 100%;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.title("🌱 FarmShield AI")
st.write("Login to continue")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    st.session_state.logged_in = True
    st.success("Login Successful 🚀")
    st.switch_page("pages/2_Detection.py")

st.markdown('</div>', unsafe_allow_html=True)