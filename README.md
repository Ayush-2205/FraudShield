# FraudShield
FraudShield is a machine learning-based web application that predicts whether an insurance claim is fraudulent or genuine. It analyzes customer, vehicle and claim details using trained ML models to help insurers reduce fraud, save costs and improve decision-making. 

## Problem Statement

Insurance companies lose billions every year due to fraudulent claims. Manual verification is time-consuming, error-prone, and inefficient. There is a need for an intelligent system that can automatically assess risk and flag suspicious claims early in the process.

---

## Solution Overview

Fraud Shield uses a machine learning model trained on historical insurance data to:
- Analyze user-provided claim details.
- Predict the likelihood of fraud.
- Provide an instant risk classification with explanation.
- Offer a clean and intuitive web interface for real-time usage.

---

## Key Features

-  Real-time fraud risk prediction  
-  Machine Learning based classification  
-  Simple and intuitive user interface  
-  Fast and lightweight Flask backend  
-  Scalable architecture for future enhancements  

---

## Technology Stack

### Frontend
- HTML5  
- CSS3  
- Responsive UI design  

### Backend
- Python  
- Flask (Web Framework)

### Machine Learning
- Scikit-learn  
- Pandas  
- NumPy  
- Joblib (Model serialization)

---

## Input Parameters

The system takes the following inputs from the user:

1. **Policy Premium** – Amount paid for the insurance policy  
2. **Total Claim Amount** – Total claim requested  
3. **Age** – Age of the policy holder  
4. **Months As Customer** – Months since he/she is enrolled into the policy

---

## Output

The model returns:
- **Low Risk: Legitimate Claim**  
  or  
- **High Risk: Potential Fraud**



---

## System Architecture

User → Web Interface → Flask Server → ML Model → Prediction → Result Display

---

## How to Run the Project

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/fraud-shield.git
cd fraud-shield

Step 2: Install dependencies

pip install -r requirements.txt

Step 3: Run the application

python app.py

Step 4: Open in browser

http://127.0.0.1:5000/
