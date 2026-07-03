import streamlit as st

st.set_page_config(page_title="About FarmShield", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#0f172a,#111827);
    color: white;
}

.title {
    font-size: 42px;
    font-weight: 700;
    color: #22c55e;
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    opacity: 0.7;
    font-size: 16px;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    background: rgba(255,255,255,0.12);
}

.icon {
    font-size: 28px;
}

.small {
    opacity: 0.8;
    font-size: 14px;
}

.tech {
    background: rgba(34,197,94,0.15);
    padding: 12px;
    border-radius: 10px;
    margin: 5px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌱 About FarmShield AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Agriculture Pest Detection System using AI</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <div class="icon">🧠</div>
    <h3>AI Detection</h3>
    <p class="small">Uses YOLOv8 deep learning model to detect pests in real-time crop images.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <div class="icon">📊</div>
    <h3>Smart Analysis</h3>
    <p class="small">Counts pests, calculates confidence and shows risk severity levels automatically.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <div class="icon">🌿</div>
    <h3>Solutions</h3>
    <p class="small">Provides organic and chemical treatment suggestions for crop protection.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## ⚙️ Technologies Used")

st.markdown("""
<div>
<span class="tech">Python</span>
<span class="tech">Streamlit</span>
<span class="tech">YOLOv8</span>
<span class="tech">OpenCV</span>
<span class="tech">NumPy</span>
<span class="tech">PIL</span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("### 🚀 Project Goal")
st.info("To help farmers detect crop pests early and reduce crop damage using AI-based image analysis.")

st.markdown("### 👨‍🌾 Impact")
st.success("Faster detection + lower pesticide usage + smarter farming decisions.")