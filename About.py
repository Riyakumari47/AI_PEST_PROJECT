import streamlit as st

st.markdown(
    """
    <style>
    .about-header { background: linear-gradient(135deg, #1E3A8A, #3B82F6); padding: 2rem; border-radius: 15px; color: white; text-align: center; margin-bottom: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .about-card { background-color: #1F2937; padding: 1.5rem; border-radius: 15px; border-left: 5px solid #3B82F6; margin-bottom: 1.5rem; color: #E5E7EB; }
    .tech-badge { background-color: #2563EB; color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.9rem; font-weight: bold; display: inline-block; margin-right: 0.5rem; margin-top: 0.5rem; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="about-header"><h1 style="margin:0;">ℹ️ Architecture & Deployment Documentation</h1></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="about-card">
        <h3 style="color: #3B82F6; margin-top: 0;">🌟 Neural Core Abstract</h3>
        <p style="line-height: 1.6;">This decentralized Edge-AI computer vision framework processes high-resolution botanical metrics to diagnose leaf pathogens in real time. Built specifically for low-latency agricultural deployment, it scales down heavy network requirements to empower smart farm monitoring nodes.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="about-card">
        <h3 style="color: #10B981; margin-top: 0;">🎯 Technical Advantage Matrix</h3>
        <ul style="margin-left: 1.2rem; line-height: 1.6;">
            <li><b>Zero Compute Backhaul:</b> Runs inference straight inside the local hardware array.</li>
            <li><b>Precision Agriculture Optimization:</b> Custom trained explicitly on target crop clusters.</li>
            <li><b>Actionable Telemetry:</b> Bridges the gap between pure classification maps and practical crop remedies.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="about-card">
        <h3 style="color: #F59E0B; margin-top: 0;">🛠️ Active Technology Core Stack</h3>
        <div class="tech-badge">Ultralytics YOLOv8 Architecture</div>
        <div class="tech-badge">Streamlit Application Node Framework</div>
        <div class="tech-badge">Python Runtime Compiler Environment</div>
        <div class="tech-badge">PIL & OpenCV Imaging Engines</div>
    </div>
    """,
    unsafe_allow_html=True
)