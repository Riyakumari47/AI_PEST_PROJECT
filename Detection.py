import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os

# 1. Page Title and Styling
st.markdown("<h2 style='text-align: center; color: #1DB9B1;'>Crop Pest Detection & Diagnosis</h2>", unsafe_allow_html=True)

# 2. Load YOLO Model with Caching for Performance
@st.cache_resource
def load_yolo_model():
    # Make sure 'best.pt' is in your root folder or adjust the path (e.g., 'model/best.pt')
    return YOLO(r"C:\Users\91826\OneDrive\Desktop\AI_PEST_PROJECT\model\best.pt")

try:
    model = load_yolo_model()
except Exception as e:
    st.error(f"Error loading model: {e}. Please ensure 'best.pt' is in the correct directory.")
    st.stop()

# 3. Pest Treatment & Recommendation Database
# Note: Replace "Tomato_Late_Blight" and "Aphids" with the exact class names your model was trained on!
pest_details = {
    "Tomato_Late_Blight": {
        "severity": "High (Immediate Attention Required)",
        "home_remedies": "Remove and destroy infected leaves immediately. Water at the base of the plant to keep the foliage completely dry.",
        "medicines": "Apply copper-based fungicides or Mancozeb spray according to agricultural expert guidelines."
    },
    "Aphids": {
        "severity": "Medium (Early Stage)",
        "home_remedies": "Spray the plant with a mixture of neem oil and soapy water, or use a strong jet stream of water to dislodge them.",
        "medicines": "Apply systemic insecticides like Imidacloprid or Acetamiprid if the infestation is widespread."
    },
    "Healthy": {
        "severity": "None (Plant is Safe)",
        "home_remedies": "Maintain normal watering schedule and ensure adequate sunlight. No special home treatment needed.",
        "medicines": "No chemical application required. The crop is perfectly healthy."
    }
}

# 4. File Uploader Component
uploaded_file = st.file_uploader("Upload an image of your crop/leaf for analysis...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Immediately display the uploaded file to the user
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image Preview", use_container_width=True)
    
    # Save image temporarily so YOLO can access the filepath
    temp_path = "temp_test_image.jpg"
    image.save(temp_path)
    
    st.markdown("---")
    
    # 5. Execution Button
    if st.button("🔴 Run Detection", use_container_width=True):
        with st.spinner("Model is analyzing the image for structural anomalies... Please wait..."):
            
            # Run YOLO prediction with an honest threshold (conf=0.35 captures early-stage threats)
            results = model(temp_path, conf=0.35, iou=0.45)
            
            # Process and display results
            for r in results:
                res_plotted = r.plot()  # Plotted image containing bounding boxes
                predicted_image = Image.fromarray(res_plotted[:, :, ::-1])  # Convert BGR to RGB
                
                # Display output image showing precisely where the pests are located
                st.subheader("🔍 Detection Visualization")
                st.image(predicted_image, caption="Identified Pest Locations (Bounding Boxes)", use_container_width=True)
                
                boxes = r.boxes
                total_detected = len(boxes)
                
                st.markdown("---")
                st.subheader("📊 Crop Health Metrics")
                
                if total_detected == 0:
                    # Honest evaluation: Nothing found means the crop is 100% safe
                    st.success("✅ Clean Scan! No pests or diseases were found. The plant is SAFE.")
                    st.metric(label="Safety Level", value="100% Safe", delta="Healthy")
                else:
                    # Infestation found
                    st.error(f"⚠️ Warning: Infection detected! Found anomalies in {total_detected} locations.")
                    
                    detected_classes = []
                    # Breakdown individual confidence metrics and locations honestly
                    for i, box in enumerate(boxes):
                        class_id = int(box.cls)
                        label = model.names[class_id]
                        confidence = float(box.conf) * 100
                        detected_classes.append(label)
                        
                        st.markdown(f"**Location #{i+1}:** Detected: `{label}` | **Confidence Score:** `{confidence:.2f}%`")
                    
                    st.markdown("---")
                    st.subheader("💊 Treatment & Recommendation Plan")
                    
                    # Deduplicate classes to avoid repeating treatment cards for the same pest
                    unique_pests = list(set(detected_classes))
                    
                    for pest in unique_pests:
                        st.markdown(f"### Infestation Name: <span style='color:#FF4B4B;'>{pest}</span>", unsafe_allow_html=True)
                        
                        # Fetch matching recommendations or fall back to default advice
                        details = pest_details.get(pest, {
                            "severity": "Medium",
                            "home_remedies": "Isolate the plant, remove infected leaves, and spray organic neem extract.",
                            "medicines": "Consult an agricultural extension worker for appropriate commercial chemical recommendations."
                        })
                        
                        # Display clean, grid-based column cards for remedies
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.info(f"**Severity Level:**\n\n{details['severity']}")
                        with col2:
                            st.warning(f"**Home Remedies:**\n\n{details['home_remedies']}")
                        with col3:
                            st.success(f"**Recommended Medicine:**\n\n{details['medicines']}")
                            
            # Clean up the temporary local file after execution completes
            if os.path.exists(temp_path):
                os.remove(temp_path)