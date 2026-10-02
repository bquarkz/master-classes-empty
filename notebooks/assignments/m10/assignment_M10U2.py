"""
M10 PMLS - Assignment 2
Developing API For Excel

Run locally with:
    uvicorn assignment_M10U2:app --reload

Deploy on Render with:
    Start command -> uvicorn assignment_M10U2:app --host 0.0.0.0 --port $PORT
"""

from fastapi import FastAPI

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
    return {"message": "Skin Clinic Campaign Analysis API is running"}

# -------------------------------------------------
# Synthetic campaign dataset
# -------------------------------------------------
def generate_campaign_data(n_customers: int = 10000, seed: int = 42) -> pd.DataFrame:

    rng = np.random.default_rng(seed)

    customer_id = [f"CUST_{100000 + i}" for i in range(n_customers)]
    gender = rng.choice(["Male", "Female"], size=n_customers, p=[0.45, 0.55])
    age = rng.integers(18, 75, size=n_customers)
    purchase_last_quarter = rng.choice(["Yes", "No"], size=n_customers, p=[0.4, 0.6])
    products_purchased_last_year = rng.integers(1, 13, size=n_customers)

    # Base response probability biased by segment so the tables show meaningful differences
    response_prob = np.full(n_customers, 0.12)
    response_prob += np.where(gender == "Female", 0.06, 0.0)
    response_prob += np.where(age < 30, 0.05, 0.0)
    response_prob += np.where(age > 50, 0.03, 0.0)
    response_prob += np.where(purchase_last_quarter == "Yes", 0.10, 0.0)
    response_prob += np.where(products_purchased_last_year > 8, 0.08, 0.0)
    response_prob += np.where(products_purchased_last_year <= 4, -0.04, 0.0)
    response_prob = np.clip(response_prob, 0.02, 0.9)

    campaign_response = rng.binomial(1, response_prob)

    return pd.DataFrame({
        "customer_id": customer_id,
        "gender": gender,
        "age": age,
        "purchase_last_quarter": purchase_last_quarter,
        "products_purchased_last_year": products_purchased_last_year,
        "campaign_response": campaign_response,
    })


CAMPAIGN_DF = generate_campaign_data()

# -------------------------------------------------
# Helper to build a response-rate (%) table for one segment
# -------------------------------------------------
def response_rate_rows(df: pd.DataFrame, segment_type: str, group_col: str) -> pd.DataFrame:

    table = (
        df.groupby(group_col, observed=True)["campaign_response"]
        .agg(customers="count", responders="sum")
        .reset_index()
        .rename(columns={group_col: "segment_value"})
    )
    table["response_rate_%"] = (table["responders"] / table["customers"] * 100).round(2)
    table.insert(0, "segment_type", segment_type)

    return table

# -------------------------------------------------
# Build the four analyses as rows of a single flat table
# -------------------------------------------------
def generate_campaign_summary() -> pd.DataFrame:

    df = CAMPAIGN_DF.copy()

    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 29, 50, np.inf],
        labels=["<30", "30-50", ">50"],
    )
    df["product_usage_group"] = pd.cut(
        df["products_purchased_last_year"],
        bins=[0, 4, 8, np.inf],
        labels=["1-4", "5-8", ">8"],
    )

    tables = [
        response_rate_rows(df, "Gender", "gender"),
        response_rate_rows(df, "Age Group", "age_group"),
        response_rate_rows(df, "Purchase Last Quarter", "purchase_last_quarter"),
        response_rate_rows(df, "Product Usage", "product_usage_group"),
    ]

    return pd.concat(tables, ignore_index=True)

# -------------------------------------------------
# API endpoint for Excel / Google Sheets / Power Query usage
# -------------------------------------------------
@app.get("/campaign-analysis")
def campaign_analysis_summary():
    try:
        df = generate_campaign_summary()

        # Handle invalid values
        df = df.replace([np.inf, -np.inf], np.nan)
        df = df.fillna(0)

        # Return JSON as a flat list of records (one row per segment value)
        return df.to_dict(orient="records")

    except Exception as e:
        return {"error": str(e)}
