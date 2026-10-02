"""
M10 PMLS - Final Exam (Assignment)
Q3. FastAPI Deployment with Excel Integration

Run locally with:
    uvicorn assignment_M10Final_Q3:app --reload

Deploy on Render with:
    Start command -> uvicorn assignment_M10Final_Q3:app --host 0.0.0.0 --port $PORT
"""

from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import numpy as np
import pandas as pd

# -------------------------------------------------
# Create FastAPI app
# -------------------------------------------------
app = FastAPI()

# -------------------------------------------------
# Health check endpoint
# -------------------------------------------------
@app.get("/health")
def health_check():
    return {"message": "Bank Loan Default Prediction API is running"}

# -------------------------------------------------
# Load data and train the Random Forest model
# -------------------------------------------------
FEATURE_COLUMNS = ["AGE", "EMPLOY", "ADDRESS", "DEBTINC", "CREDDEBT", "OTHDEBT"]
TARGET_COLUMN = "DEFAULTER"

TRAIN_DATA_PATH = Path(__file__).parent / "BANK LOAN.csv"
TEST_DATA_PATH = Path(__file__).parent / "TestData.csv"


def train_model():

    df = pd.read_csv(TRAIN_DATA_PATH)
    df = df.drop(columns=["SN"])

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(n_estimators=500, random_state=42)
    model.fit(X_train, y_train)

    valid_accuracy = accuracy_score(y_valid, model.predict(X_valid))

    # Refit on the full training dataset so predictions use all available labeled data
    model.fit(X, y)

    return model, valid_accuracy


MODEL, VALIDATION_ACCURACY = train_model()

# -------------------------------------------------
# Endpoint reporting model training info
# -------------------------------------------------
@app.get("/model-info")
def model_info():
    return {
        "model": "RandomForestClassifier",
        "n_estimators": 500,
        "features": FEATURE_COLUMNS,
        "target": TARGET_COLUMN,
        "holdout_validation_accuracy": round(float(VALIDATION_ACCURACY), 4),
    }

# -------------------------------------------------
# Score the BankLoan test dataset
# -------------------------------------------------
def score_test_dataset() -> pd.DataFrame:

    test_df = pd.read_csv(TEST_DATA_PATH)

    X_test = test_df[FEATURE_COLUMNS]
    probability_of_default = MODEL.predict_proba(X_test)[:, 1]

    result = test_df[["SN"] + FEATURE_COLUMNS].copy()
    result["probability_of_default"] = np.round(probability_of_default, 4)

    return result

# -------------------------------------------------
# Prediction endpoint called by the Submit button:
# scores every customer in the BankLoan test dataset
# -------------------------------------------------
@app.get("/predict")
def predict_test_dataset():
    try:
        result = score_test_dataset()
        return result.to_dict(orient="records")

    except Exception as e:
        return {"error": str(e)}

# -------------------------------------------------
# Request schema for scoring a single, ad-hoc customer
# -------------------------------------------------
class CustomerInfo(BaseModel):
    AGE: int
    EMPLOY: int
    ADDRESS: int
    DEBTINC: float
    CREDDEBT: float
    OTHDEBT: float

# -------------------------------------------------
# Optional endpoint to score one customer entered manually
# -------------------------------------------------
@app.post("/predict-customer")
def predict_single_customer(customer: CustomerInfo):
    try:
        X_new = pd.DataFrame([customer.model_dump()])[FEATURE_COLUMNS]
        probability_of_default = MODEL.predict_proba(X_new)[0][1]

        return {
            "probability_of_default": round(float(probability_of_default), 4)
        }

    except Exception as e:
        return {"error": str(e)}
