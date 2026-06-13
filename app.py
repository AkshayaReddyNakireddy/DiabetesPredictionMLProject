import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Diabetes Prediction System",
    page_icon="🩺",
    layout="wide"
)

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

h1{
    color:#0066cc;
    text-align:center;
}

div[data-testid="stMetric"]{
    background-color:white;
    padding:15px;
    border-radius:10px;
    border:1px solid #dcdcdc;
}
            div[data-baseweb="input"]{
    border:2px solid #0F62FE;
    border-radius:10px;
    padding:4px;
}

label{
    font-size:16px !important;
    font-weight:bold !important;
}

</style>
""",unsafe_allow_html=True)

# -------------------------------------------------
# Load Model
# -------------------------------------------------

try:

    model = joblib.load("models/diabetes_model.pkl")

    scaler = joblib.load("models/scaler.pkl")

except:

    st.error("Model files not found.")

    st.stop()

# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("🩺 AI Diabetes Prediction System")

st.markdown(
"""
Predict diabetes risk using Machine Learning based on patient health parameters.
"""
)

st.markdown("---")

# -------------------------------------------------
# Input
# -------------------------------------------------

st.markdown("## 📝 Patient Information")

col1, col2 = st.columns(2)

with col1:

    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )

    glucose = st.number_input(
        "Glucose (mg/dL)",
        min_value=0,
        max_value=300,
        value=100,
        step=1
    )

    blood_pressure = st.number_input(
        "Blood Pressure (mmHg)",
        min_value=0,
        max_value=200,
        value=70,
        step=1
    )

    skin_thickness = st.number_input(
        "Skin Thickness (mm)",
        min_value=0,
        max_value=100,
        value=20,
        step=1
    )

with col2:

    insulin = st.number_input(
        "Insulin (μU/mL)",
        min_value=0,
        max_value=900,
        value=80,
        step=1
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=70.0,
        value=25.0,
        step=0.1,
        format="%.1f"
    )

    dpf = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.500,
        step=0.001,
        format="%.3f"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30,
        step=1
    )

st.markdown("---")

# -------------------------------------------------
# Predict
# -------------------------------------------------

if st.button("🔍 Predict Diabetes Risk",use_container_width=True):

    input_df=pd.DataFrame({

        "Pregnancies":[pregnancies],

        "Glucose":[glucose],

        "BloodPressure":[blood_pressure],

        "SkinThickness":[skin_thickness],

        "Insulin":[insulin],

        "BMI":[bmi],

        "DiabetesPedigreeFunction":[dpf],

        "Age":[age]

    })

    scaled=scaler.transform(input_df)

    prediction=model.predict(scaled)

    probability=model.predict_proba(scaled)[0][1]

    st.markdown("---")

    c1,c2,c3=st.columns(3)

    c1.metric(
        "Age",
        age
    )

    c2.metric(
        "BMI",
        bmi
    )

    c3.metric(
        "Glucose",
        glucose
    )

    st.markdown("---")

    st.subheader("Prediction Result")

    if probability<0.30:

        st.success("🟢 Low Risk")

    elif probability<0.70:

        st.warning("🟡 Moderate Risk")

    else:

        st.error("🔴 High Risk")

    st.metric(

        "Risk Probability",

        f"{probability*100:.2f}%"

    )

    st.progress(float(probability))

    st.markdown("---")

    st.subheader("Patient Summary")

    summary=pd.DataFrame({

        "Feature":[

            "Pregnancies",

            "Glucose",

            "Blood Pressure",

            "Skin Thickness",

            "Insulin",

            "BMI",

            "DPF",

            "Age"

        ],

        "Value":[

            pregnancies,

            glucose,

            blood_pressure,

            skin_thickness,

            insulin,

            bmi,

            dpf,

            age

        ]

    })

    st.dataframe(summary,use_container_width=True)

    st.markdown("---")

    st.subheader("Health Recommendation")

    if bmi>30:

        st.warning("⚠ BMI is high. Consider weight management.")

    elif bmi<18.5:

        st.info("BMI indicates underweight.")

    else:

        st.success("Healthy BMI range.")

    if glucose>=126:

        st.error("High glucose level detected.")

    elif glucose>=100:

        st.warning("Prediabetes glucose range.")

    else:

        st.success("Normal glucose level.")

    st.markdown("---")

    st.subheader("Feature Importance")

    features=[

        "Pregnancies",

        "Glucose",

        "BloodPressure",

        "SkinThickness",

        "Insulin",

        "BMI",

        "DPF",

        "Age"

    ]

    importance=model.feature_importances_

    fig,ax=plt.subplots(figsize=(8,4))

    ax.barh(features,importance)

    ax.set_xlabel("Importance")

    st.pyplot(fig)

    st.markdown("---")

    csv=summary.to_csv(index=False)

    st.download_button(

        "📄 Download Patient Report",

        csv,

        file_name="patient_report.csv",

        mime="text/csv"

    )



# -------------------------------------------------
# Footer
# -------------------------------------------------

st.markdown("---")

st.info(
"""
**Disclaimer:** This application is intended for educational purposes only.
The prediction is generated by a Machine Learning model and should not be
considered a medical diagnosis. Please consult a healthcare professional for
proper evaluation and treatment.
"""
)