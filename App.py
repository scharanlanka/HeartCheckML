import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('heart_disease_model.pkl')

# Title
st.title("Heart Disease Prediction")

# Input fields
st.sidebar.header("Input Features")
age = st.sidebar.slider("Age", 29, 77, 50)
sex = st.sidebar.selectbox("Sex", [0, 1])
cp = st.sidebar.slider("Chest Pain Type", 0, 3, 1)
trestbps = st.sidebar.slider("Resting Blood Pressure", 94, 200, 120)
chol = st.sidebar.slider("Cholesterol", 126, 564, 200)
fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.sidebar.slider("Resting ECG", 0, 2, 1)
thalach = st.sidebar.slider("Maximum Heart Rate Achieved", 71, 202, 150)
exang = st.sidebar.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.sidebar.slider("ST Depression Induced by Exercise", 0.0, 6.2, 1.0)
slope = st.sidebar.slider("Slope of the Peak Exercise ST Segment", 0, 2, 1)
ca = st.sidebar.slider("Number of Major Vessels Colored by Fluoroscopy", 0, 4, 1)
thal = st.sidebar.slider("Thalassemia", 0, 3, 2)

# Create a DataFrame from inputs
input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'cp': [cp],
    'trestbps': [trestbps],
    'chol': [chol],
    'fbs': [fbs],
    'restecg': [restecg],
    'thalach': [thalach],
    'exang': [exang],
    'oldpeak': [oldpeak],
    'slope': [slope],
    'ca': [ca],
    'thal': [thal]
})

# Display input data
st.write("Input Data:")
st.write(input_data)

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write("Prediction:")
    if prediction[0] == 1:
        st.write("Heart Disease Detected")
    else:
        st.write("No Heart Disease Detected")