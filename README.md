 **Credit Risk Prediction Web App**
This project is a Flask-based web application that predicts whether a customer is likely to default on their next credit card payment. It uses a logistic regression model trained on a dataset balanced using SMOTE (Synthetic Minority Over-sampling Technique).

**🚀 Demo**
Try the live version (if hosted):
👉** https://credit-risk-app-9y67.onrender.com**

**📂 Project Structure**
.
├── app.py                 # Main Flask application
├── model.pkl              # Trained logistic regression model
├── templates/
│   └── index.html         # UI for input and prediction
├── requirements.txt       # Python dependencies
├── Procfile               # Deployment file for Render
└── README.md              # Project documentation

**🧠 Model Overview**
Algorithm: Logistic Regression (via statsmodels)

Data Balancing: SMOTE

Input Features:

LIMIT_BAL

SEX

EDUCATION

MARRIAGE

AGE

PAY_1 to PAY_6

PAY_AMT1 to PAY_AMT6

**📘 Data Dictionary**
Feature	Description
LIMIT_BAL	Credit limit 
SEX	Gender (1 = Male, 2 = Female)
EDUCATION	Education level (1 = Graduate, 2 = University, 3 = High school, 4 = Others)
MARRIAGE	Marital status (1 = Married, 2 = Single, 3 = Others)
AGE	Age of the customer
PAY_1 to PAY_6	Repayment status (0 = On time, 1–9 = Delay in months)
PAY_AMT1 to PAY_AMT6	Amount paid in respective month

**💡 Features**
User-friendly web interface

Dropdowns for categorical fields

Styled using Bootstrap 5

SweetAlert2 for beautiful prediction alerts

Responsive design

Deployed for free using Render.com

**🧪 How to Run Locally**
**1. Clone the repo:**

git clone [https://github.com/Ranjana05b/credit-risk-app.git](https://github.com/Ranjana05b/Credit_risk_app.git)
cd credit-risk-app

**2. Install dependencies:**
pip install -r requirements.txt

**3. Run the Flask app:**
python app.py
**5. Open browser and go to: http://127.0.0.1:5000**
