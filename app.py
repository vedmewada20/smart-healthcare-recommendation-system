import pickle
import numpy as np
import pandas as pd
import streamlit as st

# Set webpage tab styling configuration
st.set_page_config(
    page_title="Healthcare Recommendation System",
    layout="centered",
)

# 1. Load your downloaded pickle files
@st.cache_resource
def load_assets():
    model = pickle.load(open("treatment_rf_model.pkl", "rb"))
    features = pickle.load(open("symptom_features.pkl", "rb"))
    lookup = pd.read_pickle("medical_lookup.pkl")
    return model, features, lookup


try:
    model, symptom_features, lookup_df = load_assets()

    st.title("🏥 Smart Healthcare Recommendation System")
    st.markdown("---")

    # 2. Webpage Input Dropdown Search Box
    st.subheader("📋 Select Patient Symptoms")
    user_selections = st.multiselect(
        "Search or choose symptoms from the menu:",
        options=symptom_features,
    )

    # 3. Action Prediction Button
    if st.button("Generate Diagnostic & Treatment Plan", type="primary"):
        if not user_selections:
            st.warning("Please select at least one symptom to process analysis.")
        else:
            # Convert text input into numbers (1s and 0s) for your model
            input_vector = [
                1 if symptom in user_selections else 0
                for symptom in symptom_features
            ]
            input_array = np.array(input_vector).reshape(1, -1)

            # Predict disease using your model
            prediction = model.predict(input_array)[0]
            st.success(f"### Predicted Diagnosis: **{prediction}**")

            # Look up information from your medical database
            matched_info = lookup_df[lookup_df["Disease"] == prediction]

            if not matched_info.empty:
                info_row = matched_info.iloc[0]
                st.markdown("#### 📖 Clinical Description")
                st.write(info_row["Description"])

                st.markdown("#### 🛡️ Recommended Precautionary Steps")
                st.write(f"1. ⚠️ {info_row['Precaution_1'].capitalize()}")
                st.write(f"2. ⚠️ {info_row['Precaution_2'].capitalize()}")
                st.write(f"3. ⚠️ {info_row['Precaution_3'].capitalize()}")
                st.write(f"4. ⚠️ {info_row['Precaution_4'].capitalize()}")

except FileNotFoundError:
    st.error(
        "📁 File Error: Make sure your 3 .pkl files are placed inside the exact same folder as app.py!"
    )