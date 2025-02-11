# Heart Disease Prediction using Machine Learning

## Overview

This project aims to predict heart disease using a Machine Learning model trained on a medical dataset. The application is built with Streamlit to provide an interactive user interface for inputting patient data and receiving predictions.

## Features

- Exploratory Data Analysis (EDA) for insights into the dataset.
- Machine Learning model trained on structured medical data.
- Streamlit-based web application for easy interaction.
- Real-time predictions based on user inputs.

## Dataset

The dataset used in this project contains medical attributes such as age, sex, cholesterol levels, blood pressure, and more. It helps predict the likelihood of heart disease.

## Tech Stack

- **Programming Language**: Python
- **Libraries Used**: Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, Streamlit, Joblib
- **Deployment**: Streamlit

## Installation

### Prerequisites

Ensure you have Python installed (>=3.7). Install the required libraries using:

```bash
pip install -r requirements.txt
```

## Usage
### 1. Clone the repository

```bash
git clone https://github.com/scharanlanka/HeartCheckML
```

### 2. Install the dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```
#### Input Features
- Age, sex, cholesterol, blood pressure, and other medical attributes.
- Click the Predict button to get a result.
#### Output
- "Heart Disease Detected" if the model predicts a high risk.
- "No Heart Disease Detected" if the model predicts a low risk.
