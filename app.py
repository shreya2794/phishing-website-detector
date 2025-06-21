import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Phishing Detector", page_icon="🛡️")
st.title("🛡️ Phishing Website Detection using dataset from kaggle")

# Load trained model
model = joblib.load("model/phishing_model.pkl")
expected_columns = list(model.feature_names_in_)

# Upload test file
uploaded_file = st.file_uploader("📂 Upload test CSV (no 'class' column)", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    
    # Drop "Index" column if present
    data = data.drop("Index", axis=1, errors="ignore")
    
    # Check column match
    if not all(col in data.columns for col in expected_columns):
        st.error("🚫 Uploaded file is missing required features.")
        st.markdown(f"**Expected columns:** {expected_columns}")
        st.stop()

    # Ensure correct column order
    data = data[expected_columns]

    # Predict
    predictions = model.predict(data)
    # Handle probability safely
    try:
       probabilities = model.predict_proba(data)[:, 1]  # Prob of phishing
       confidences = (probabilities * 100).round(2).astype(str) + " %"
    except:
       confidences = ["N/A"] * len(predictions)

    # Add results
    data["Prediction"] = np.where(predictions == 1, "🔴 Phishing", "🟢 Legitimate")
    data["Confidence"] = confidences

    # Show output
    st.success(f"✅ Predictions complete. Total: {len(predictions)}")
    st.dataframe(data)

    # Show summary
    phishing_count = sum(predictions)
    st.markdown(f"**🔴 Phishing Detected:** {phishing_count} / {len(predictions)}")
