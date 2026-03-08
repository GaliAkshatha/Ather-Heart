#  Ather Heart – Heart Disease Prediction System

Ather Heart is a **machine learning powered web application** that predicts the risk of heart disease using patient health parameters.

The system includes **OCR-based report extraction, manual form prediction, explainable AI insights (SHAP), and role-based dashboards** for patients, doctors, and hospitals.

The goal of this project is to make **early heart disease risk screening accessible, explainable, and interactive** using AI and modern web technologies.

---

#  Features

##  Patient Interface
- Upload medical reports (OCR extracts values automatically)
- Manual health parameter input form
- Heart disease **risk classification (Low / Medium / High)**
- **Probability score** of prediction
- SHAP-based friendly explanations
- Health recommendation cards based on risk
- Floating chatbot assistant (**Chopper**)

---

##  Doctor Interface
- View prediction details
- Raw **SHAP feature contributions**
- Feature importance for each patient prediction

---

##  Hospital Interface
- Basic administrative dashboard
- Placeholder for future hospital integration

---

#  Machine Learning Pipeline

### Data Processing
- Combined dataset created by merging multiple heart disease datasets
- Missing value removal
- BMI feature generation
- StandardScaler normalization
- SMOTE for class imbalance handling

### Model
- **XGBoost Classifier**
- Optimized hyperparameters

### Explainability
- **SHAP (SHapley Additive exPlanations)** used to explain predictions.

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
- SHAP
- Tesseract OCR
- Joblib
- Flask-CORS

## Machine Learning
- XGBoost
- Scikit-learn
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
│   ├── ocr_utils.py
│   ├── preprocess_utils.py
│   ├── requirements.txt
│
│   └── model
│       ├── heart_model.pkl
│       ├── scaler.pkl
│       ├── feature_columns.pkl
│
│       └── training
│           ├── combined.csv
│           └── train_model.py
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   └── assets
│   └── package.json
│
└── README.md
```

---

#  Installation & Setup

## 1️ Clone the Repository

```bash
git clone https://github.com/GaliAkshatha/Ather-Heart.git
cd Ather-Heart
```

---

## 2️ Backend Setup

```bash
cd backend

python -m venv venv

# Activate environment

# Windows
venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

Backend runs at:

```
http://127.0.0.1:5000
```

---

## 3️ Frontend Setup

Open a new terminal:

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

#  Sample Input for Testing

Use the following values in the manual prediction form:

| Parameter | Value |
|-----------|-------|
| Age | 54 |
| Sex | 1 |
| Height | 165 |
| Weight | 78 |
| RestingBP | 150 |
| DiastolicBP | 95 |
| Cholesterol | 240 |
| Glucose | 130 |
| Smoking | 0 |
| AlcoholIntake | 1 |
| PhysicalActivity | 2 |

Expected Output:

- **High Risk**
- Probability around **80–90%**
- SHAP explanation
- Health recommendations

---


