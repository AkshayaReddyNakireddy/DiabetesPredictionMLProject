<<<<<<< HEAD
# 🩺 Diabetes Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a person is at risk of diabetes using Machine Learning based on medical parameters such as glucose level, BMI, age, blood pressure, insulin level, and other health indicators.

The application is built using **Python, Scikit-learn, and Streamlit** and provides an easy-to-use web interface for making predictions.

---

## 🚀 Features

- Predicts diabetes risk using a trained Random Forest model
- User-friendly Streamlit interface
- Data preprocessing with StandardScaler
- Displays prediction result and probability
- Trained on the Pima Indians Diabetes Dataset

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 📂 Project Structure

```
DiabetesPredictionMLProject/
│
├── data/
│   └── diabetes.csv
│
├── models/
│   ├── diabetes_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│
├── train.py
├── app.py
├── predict.py
├── EDA.ipynb
├── requirements.txt
├── README.md
└── venv/
```

---

## 📊 Dataset

The project uses the **Pima Indians Diabetes Dataset**.

### Input Features

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

### Target

- 0 → No Diabetes
- 1 → Diabetes

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/DiabetesPredictionMLProject.git
```

Move into the project folder

```bash
cd DiabetesPredictionMLProject
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
python train.py
```

This will generate:

```
models/
├── diabetes_model.pkl
└── scaler.pkl
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the browser and visit

```
http://localhost:8501
```

---

## 📈 Machine Learning Pipeline

```
Dataset
   │
   ▼
Data Preprocessing
   │
   ▼
Train-Test Split
   │
   ▼
Feature Scaling
   │
   ▼
Random Forest Classifier
   │
   ▼
Model Evaluation
   │
   ▼
Save Model (.pkl)
   │
   ▼
Streamlit Web Application
```

---

## 📊 Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 📷 Application Preview

Add screenshots of your Streamlit application inside an **images/** folder and reference them here.

---

## 🔮 Future Improvements

- XGBoost implementation
- Feature importance visualization
- Risk probability gauge
- Explainable AI (SHAP)
- Cloud deployment
- PDF health report generation

---

## 👩‍💻 Author

**Akshaya N**

Final Year Electronics and Communication Engineering Student

Interested in Machine Learning, VLSI, Embedded Systems, and AI Applications.

---

## 📄 License

This project is developed for educational and portfolio purposes.
=======
# 🩺 Diabetes Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a person is at risk of diabetes using Machine Learning based on medical parameters such as glucose level, BMI, age, blood pressure, insulin level, and other health indicators.

The application is built using **Python, Scikit-learn, and Streamlit** and provides an easy-to-use web interface for making predictions.

---

## 🚀 Features

- Predicts diabetes risk using a trained Random Forest model
- User-friendly Streamlit interface
- Data preprocessing with StandardScaler
- Displays prediction result and probability
- Trained on the Pima Indians Diabetes Dataset

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 📂 Project Structure

```
DiabetesPredictionMLProject/
│
├── data/
│   └── diabetes.csv
│
├── models/
│   ├── diabetes_model.pkl
│   └── scaler.pkl
│
│
├── train.py
├── app.py
├── predict.py
├── requirements.txt
├── README.md
└── venv/
```

---

## 📊 Dataset

The project uses the **Pima Indians Diabetes Dataset**.

### Input Features

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

### Target

- 0 → No Diabetes
- 1 → Diabetes

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/DiabetesPredictionMLProject.git
```

Move into the project folder

```bash
cd DiabetesPredictionMLProject
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
python train.py
```

This will generate:

```
models/
├── diabetes_model.pkl
└── scaler.pkl
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the browser and visit

```
http://localhost:8501
```

---

## 📈 Machine Learning Pipeline

```
Dataset
   │
   ▼
Data Preprocessing
   │
   ▼
Train-Test Split
   │
   ▼
Feature Scaling
   │
   ▼
Random Forest Classifier
   │
   ▼
Model Evaluation
   │
   ▼
Save Model (.pkl)
   │
   ▼
Streamlit Web Application
```

---

## 📊 Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 📷 Application Preview

Add screenshots of your Streamlit application inside an **images/** folder and reference them here.

---

## 🔮 Future Improvements

- XGBoost implementation
- Feature importance visualization
- Risk probability gauge
- Explainable AI (SHAP)
- Cloud deployment
- PDF health report generation

---


---

## 📄 License

This project is developed for educational and portfolio purposes.
>>>>>>> eef19620bcf3ea87b079881a2d790e948bed2bfd
