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

col1,col2=st.columns(2)

with col1:

    pregnancies=st.slider(
        "Pregnancies",
        0,
        20,
        1
    )

    glucose=st.slider(
        "Glucose",
        0,
        300,
        120
    )

    blood_pressure=st.slider(
        "Blood Pressure",
        0,
        200,
        70
    )

    skin_thickness=st.slider(
        "Skin Thickness",
        0,
        100,
        20
    )

with col2:

    insulin=st.slider(
        "Insulin",
        0,
        900,
        80
    )

    bmi=st.slider(
        "BMI",
        0.0,
        70.0,
        25.0
    )

    dpf=st.slider(
        "Diabetes Pedigree Function",
        0.0,
        3.0,
        0.50
    )

    age=st.slider(
        "Age",
        1,
        120,
        30
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