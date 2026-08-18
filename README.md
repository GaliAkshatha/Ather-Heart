# ❤️ Ather Heart – AI-Powered Heart Disease Prediction System

<p align="center">

![React](https://img.shields.io/badge/React-19-blue?logo=react)
![Flask](https://img.shields.io/badge/Flask-Python-black?logo=flask)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-success)
![SHAP](https://img.shields.io/badge/Explainable%20AI-SHAP-orange)
![OCR](https://img.shields.io/badge/OCR-Tesseract-blueviolet)
![License](https://img.shields.io/badge/Status-Active-success)

</p>

An AI-powered healthcare web application that predicts the risk of heart disease using Machine Learning while providing transparent, explainable predictions through SHAP.

The application combines OCR-based medical report extraction, manual health parameter prediction, and role-based dashboards to provide an interactive and explainable heart disease screening experience.

---

#  Live Demo

[https://ather.akshathag.in](https://ather.akshathag.in)

---

#  Features

##  Patient Portal

- OCR-based medical report upload
- Automatic extraction of medical values
- Manual health parameter input
- Heart disease prediction
- Risk classification
  - Low
  - Medium
  - High
- Prediction probability
- Explainable AI using SHAP
- Personalized health recommendations
- Floating AI chatbot assistant (Chopper)

---

##  Doctor Portal

- View patient prediction details
- SHAP feature contribution visualization
- Feature importance explanation
- Clinical prediction summary

---

##  Hospital Portal

- Administrative dashboard
- Foundation for future hospital integration

---

#  Machine Learning Pipeline

## Data Processing

- Combined multiple heart disease datasets
- Data cleaning
- Missing value removal
- BMI feature generation
- StandardScaler normalization
- SMOTE class balancing

## Model

- XGBoost Classifier
- Hyperparameter tuning
- Probability-based prediction

## Explainable AI

Predictions are explained using:

- SHAP (SHapley Additive Explanations)

allowing users and doctors to understand why a prediction was made instead of receiving a black-box result.

---

#  Tech Stack

## Frontend

- React (Vite)
- Tailwind CSS
- JavaScript
- Axios

## Backend

- Flask
- Python
- Flask-CORS
- Tesseract OCR
- Joblib

## Machine Learning

- XGBoost
- Scikit-learn
- SHAP
- Pandas
- NumPy
- Imbalanced-learn (SMOTE)

---

#  Project Structure

```
Ather-Heart
│
├── backend
│   ├── app.py
│   ├── predict.py
│   ├── preprocess_utils.py
│   ├── ocr_utils.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── model
│       ├── heart_model.pkl
│       ├── scaler.pkl
│       ├── feature_columns.pkl
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
└── README.md
```

---

#  Installation

## Clone Repository

```bash
git clone https://github.com/GaliAkshatha/Ather-Heart.git

cd Ather-Heart
```

---

## Backend

```bash
cd backend

python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python app.py
```

Backend

```
http://127.0.0.1:5000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend

```
http://localhost:5173
```

---

#  Sample Test Input

| Parameter | Value |
|-----------|------:|
| Age | 54 |
| Sex | 1 |
| Height | 165 |
| Weight | 78 |
| RestingBP | 150 |
| DiastolicBP | 95 |
| Cholesterol | 240 |
| Glucose | 130 |
| Smoking | 0 |
| Alcohol Intake | 1 |
| Physical Activity | 2 |

Expected Result

- High Risk
- Probability around 80–90%
- SHAP explanation
- Health recommendations

---

#  Deployment

Frontend

- Vercel

Backend

- Render (Docker)

---

#  Future Improvements

- Secure authentication
- Doctor-patient history
- Hospital database integration
- PDF report generation
- Email notifications
- Multi-language support
- Appointment scheduling
- Cloud database support


