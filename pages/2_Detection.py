import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
from fpdf import FPDF

st.set_page_config(page_title="FarmShield AI", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b);
    color: white;
}

.big-card {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return YOLO("model/best.pt")

model = load_model()

SOLUTIONS = {
    "beetle": {
        "organic": ["Neem oil spray", "Remove infected leaves", "Sticky traps"],
        "chemical": ["Imidacloprid", "Spinosad", "Cypermethrin"]
    }
}

st.title("🌱 FarmShield AI Detection System")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    results = model.predict(np.array(image), conf=0.25, verbose=False)
    r = results[0]

    img = r.plot()
    st.image(img, caption="Detection Result", use_container_width=True)

    boxes = r.boxes
    count = len(boxes)

    if count > 0:
        conf = float(max(boxes.conf)) * 100
        pest = model.names[int(boxes.cls[0])]
    else:
        conf = 0
        pest = "No Pest Detected"

    # ✅ FIXED RISK LOGIC (your requirement)
    if count <= 2:
        level = "SAFE"
        color = "green"
        progress = 20

    elif count < 5:
        level = "MODERATE"
        color = "orange"
        progress = 60

    else:
        level = "HIGH RISK"
        color = "red"
        progress = 90

    st.subheader("📊 Detection Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Pest Name", pest)

    with col2:
        st.metric("Count", count)

    with col3:
        st.metric("Confidence", f"{conf:.2f}%")

    st.markdown(f"### Risk Level: <span style='color:{color}'>{level}</span>", unsafe_allow_html=True)

    st.progress(progress)

    st.markdown("## 🌿 Remedies")

    if pest in SOLUTIONS:
        for i in SOLUTIONS[pest]["organic"]:
            st.success("🌱 " + i)

        for i in SOLUTIONS[pest]["chemical"]:
            st.error("🧪 " + i)

    # ✅ PDF
    def pdf_report():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200,10,"FarmShield AI Report",ln=True)
        pdf.cell(200,10,f"Pest: {pest}",ln=True)
        pdf.cell(200,10,f"Count: {count}",ln=True)
        pdf.cell(200,10,f"Confidence: {conf:.2f}%",ln=True)
        pdf.cell(200,10,f"Risk: {level}",ln=True)

        return pdf.output(dest="S").encode("latin-1")

    st.download_button(
        "📄 Download Report",
        data=pdf_report(),
        file_name="FarmShield_Report.pdf"
    )