# train.py

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/diabetes.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Define Features and Target
# -----------------------------
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# Feature Scaling
# -----------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# Train Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train_scaled, y_train)

# -----------------------------
# Make Predictions
# -----------------------------
y_pred = model.predict(X_test_scaled)

# -----------------------------
# Evaluate Model
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("Model Accuracy:", round(accuracy * 100, 2), "%")
print("==============================\n")

print("Classification Report:\n")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# -----------------------------
# Save Model and Scaler
# -----------------------------
joblib.dump(model, "models/diabetes_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("\nModel saved successfully!")
print("Files created:")
print("models/diabetes_model.pkl")
print("models/scaler.pkl")