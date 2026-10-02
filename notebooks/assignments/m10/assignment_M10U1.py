"""
M10 PMLS - Assignment 1
Model Deployment Using FastAPI

Run locally with:
    uvicorn assignment_M10U1:app --reload

Deploy on Render with:
    Start command -> uvicorn assignment_M10U1:app --host 0.0.0.0 --port $PORT
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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
# Helper to build a response-rate (%) table
# -------------------------------------------------
def response_rate_table(df: pd.DataFrame, group_col: str) -> pd.DataFrame:

    table = (
        df.groupby(group_col, observed=True)["campaign_response"]
        .agg(customers="count", responders="sum")
        .reset_index()
    )
    table["response_rate_%"] = (table["responders"] / table["customers"] * 100).round(2)

    return table

# -------------------------------------------------
# Task 1: Gender vs Campaign Response
# -------------------------------------------------
def gender_vs_response(df: pd.DataFrame) -> pd.DataFrame:
    return response_rate_table(df, "gender")

# -------------------------------------------------
# Task 2: Age Group vs Campaign Response
# -------------------------------------------------
def age_group_vs_response(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 29, 50, np.inf],
        labels=["<30", "30-50", ">50"],
    )

    return response_rate_table(df, "age_group")

# -------------------------------------------------
# Task 3: Purchase in Last Quarter vs Campaign Response
# -------------------------------------------------
def purchase_last_quarter_vs_response(df: pd.DataFrame) -> pd.DataFrame:
    return response_rate_table(df, "purchase_last_quarter")

# -------------------------------------------------
# Task 4: Product Usage vs Campaign Response
# -------------------------------------------------
def product_usage_vs_response(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()
    df["product_usage_group"] = pd.cut(
        df["products_purchased_last_year"],
        bins=[0, 4, 8, np.inf],
        labels=["1-4", "5-8", ">8"],
    )

    return response_rate_table(df, "product_usage_group")

# -------------------------------------------------
# Build all four analysis tables
# -------------------------------------------------
def build_campaign_analysis(df: pd.DataFrame) -> dict:

    return {
        "gender_vs_response": gender_vs_response(df).to_dict(orient="records"),
        "age_group_vs_response": age_group_vs_response(df).to_dict(orient="records"),
        "purchase_last_quarter_vs_response": purchase_last_quarter_vs_response(df).to_dict(orient="records"),
        "product_usage_vs_response": product_usage_vs_response(df).to_dict(orient="records"),
    }

# -------------------------------------------------
# API endpoint returning JSON data
# -------------------------------------------------
@app.get("/campaign-analysis")
def get_campaign_analysis():
    return build_campaign_analysis(CAMPAIGN_DF)

# -------------------------------------------------
# HTML frontend embedded directly in endpoint
# -------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def home():

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Skin Clinic Campaign Analysis</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
            }
            button {
                padding: 10px 16px;
                font-size: 16px;
                margin-bottom: 20px;
                cursor: pointer;
            }
            table {
                border-collapse: collapse;
                width: 100%;
                margin-bottom: 30px;
            }
            th, td {
                border: 1px solid #ccc;
                padding: 8px;
                text-align: center;
            }
            th {
                background-color: #f4f4f4;
            }
            h3 {
                margin-bottom: 6px;
            }
        </style>
    </head>
    <body>

        <h2>Skin Clinic Campaign Analysis</h2>

        <button onclick="loadData()">Load Analysis</button>

        <h3>Gender vs Campaign Response</h3>
        <table id="genderTable">
            <thead>
                <tr><th>Gender</th><th>Customers</th><th>Responders</th><th>Response Rate (%)</th></tr>
            </thead>
            <tbody></tbody>
        </table>

        <h3>Age Group vs Campaign Response</h3>
        <table id="ageTable">
            <thead>
                <tr><th>Age Group</th><th>Customers</th><th>Responders</th><th>Response Rate (%)</th></tr>
            </thead>
            <tbody></tbody>
        </table>

        <h3>Purchase in Last Quarter vs Campaign Response</h3>
        <table id="purchaseTable">
            <thead>
                <tr><th>Purchase Last Quarter</th><th>Customers</th><th>Responders</th><th>Response Rate (%)</th></tr>
            </thead>
            <tbody></tbody>
        </table>

        <h3>Product Usage vs Campaign Response</h3>
        <table id="productTable">
            <thead>
                <tr><th>Product Usage Group</th><th>Customers</th><th>Responders</th><th>Response Rate (%)</th></tr>
            </thead>
            <tbody></tbody>
        </table>

        <script>
            function fillTable(tableId, rows, keyName) {
                const tbody = document.querySelector(`#${tableId} tbody`);
                tbody.innerHTML = '';

                rows.forEach(row => {
                    const tr = document.createElement('tr');
                    tr.innerHTML = `
                        <td>${row[keyName]}</td>
                        <td>${row.customers}</td>
                        <td>${row.responders}</td>
                        <td>${row["response_rate_%"]}</td>
                    `;
                    tbody.appendChild(tr);
                });
            }

            function loadData() {
                fetch('/campaign-analysis')
                    .then(response => response.json())
                    .then(data => {
                        fillTable('genderTable', data.gender_vs_response, 'gender');
                        fillTable('ageTable', data.age_group_vs_response, 'age_group');
                        fillTable('purchaseTable', data.purchase_last_quarter_vs_response, 'purchase_last_quarter');
                        fillTable('productTable', data.product_usage_vs_response, 'product_usage_group');
                    })
                    .catch(error => {
                        alert('Error fetching data');
                        console.error(error);
                    });
            }
        </script>

    </body>
    </html>
    """

    return html_content
