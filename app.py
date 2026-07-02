import streamlit as st

st.set_page_config(page_title="Crop Disease System", layout="wide", initial_sidebar_state="expanded")

st.markdown(
    """
    <style>
    .hero-container { background: linear-gradient(135deg, #111827, #065F46); padding: 3rem; border-radius: 20px; text-align: center; color: white; box-shadow: 0 10px 25px rgba(0,0,0,0.3); margin-bottom: 2.5rem; }
    .hero-title { font-size: 3rem; font-weight: 800; letter-spacing: -1px; margin-bottom: 1rem; color: #10B981; }
    .hero-sub { font-size: 1.3rem; color: #D1D5DB; max-width: 800px; margin: 0 auto 2rem; line-height: 1.6; }
    .step-card { background-color: #1F2937; color: #F3F4F6; padding: 1.5rem; border-radius: 15px; border-top: 4px solid #10B981; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%; transition: transform 0.2s; }
    .step-card:hover { transform: translateY(-5px); }
    .step-num { font-size: 2rem; font-weight: bold; color: #10B981; margin-bottom: 0.5rem; }
    .step-text { font-size: 1.1rem; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">🌱 Next-Gen Crop Health Analyzer</div>
        <div class="hero-sub">Empowering smart agriculture with real-time computer vision. Instantly diagnose plant diseases, identify pests, and unlock actionable agro-remedies.</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<h3 style='text-align: center; color: #E5E7EB; margin-bottom: 2rem;'>🚀 Quick Start Execution Pipeline</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-num">01</div>
            <div class="step-text">🔐 Authenticate Gateway</div>
            <p style='color: #9CA3AF; margin-top: 0.5rem;'>Navigate to the <b>Login</b> tab on the sidebar to spin up your personalized cloud instance session.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-num">02</div>
            <div class="step-text">📷 Upload Leaf Specimen</div>
            <p style='color: #9CA3AF; margin-top: 0.5rem;'>Head over to the <b>Detection</b> module and drop any clear crop leaf snapshot into the pipeline scanner.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-num">03</div>
            <div class="step-text">🔬 Fetch Instant Remedies</div>
            <p style='color: #9CA3AF; margin-top: 0.5rem;'>Trigger the AI inference matrix to overlay instant visual bounding boxes and extract targeted agro-solutions.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.sidebar.info("🎯 Use the Control Panel above to jump across edge nodes.")