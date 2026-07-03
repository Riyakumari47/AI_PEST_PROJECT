import streamlit as st
import pandas as pd
from datetime import datetime

mock_history_data = {
    "Timestamp / Date": [
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        "2026-07-01 14:22",
        "2026-06-30 09:15",
        "2026-06-28 18:40"
    ],
    "Sample Image Name": [
        "insect.jpg",
        "crop_leaf_02.png",
        "tomato_pest_scan.jpg",
        "field_quadrant_1.png"
    ],
    "Classified Pest Group": [
        "Beetles Detected",
        "Aphids Found",
        "No Pests Identified",
        "Beetles Detected"
    ],
    "Total Count": [
        12,
        4,
        0,
        18
    ],
    "Danger Status Evaluation": [
        "CRITICAL RISK 🔴",
        "LOW RISK ALERT 🟢",
        "SAFE STATUS 🟢",
        "CRITICAL RISK 🔴"
    ]
}

df_logs = pd.DataFrame(mock_history_data)

st.dataframe(df_logs, use_container_width=True, hide_index=True)