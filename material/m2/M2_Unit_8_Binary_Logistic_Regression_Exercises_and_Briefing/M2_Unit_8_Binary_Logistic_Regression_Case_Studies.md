# M2 Unit 8 – Binary Logistic Regression  
## Case Study Exercises

---

## 🎯 Learning Goals

- Apply logistic regression to binary classification problems.  
- Interpret coefficients in terms of odds ratios.  
- Evaluate models using confusion matrix, ROC, and AUC.  

---

### Case Study 1 – Customer Churn Prediction

**Context**  
A telecom company wants to predict whether a customer will **churn** (leave the service). We have:

- `tenure` (months as customer)  
- `monthly_charges`  
- `churn` (1 = churn, 0 = stay)

#### 💻 Python Part

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

np.random.seed(0)
n = 1000
tenure = np.random.exponential(scale=24, size=n)
monthly_charges = np.random.normal(50, 10, size=n)

# true logit model
logit = -2.0 - 0.03*tenure + 0.02*monthly_charges
p = 1 / (1 + np.exp(-logit))
churn = (np.random.rand(n) < p).astype(int)

df = pd.DataFrame({
    "tenure": tenure,
    "monthly_charges": monthly_charges,
    "churn": churn
})

X = df[["tenure", "monthly_charges"]]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

#### 🧮 Questions

1. Interpret the **sign** of the coefficient for `tenure` (do longer-tenure customers churn more or less?).  
2. Interpret the coefficient for `monthly_charges`.  
3. Why might accuracy be misleading if churn is rare? Which metrics are better here?

---

### Case Study 2 – Interpreting Odds Ratios

Using `statsmodels` to obtain odds ratios:

```python
import statsmodels.api as sm

X_const = sm.add_constant(X_train)
logit_model = sm.Logit(y_train, X_const).fit(disp=0)
print(logit_model.summary())

params = logit_model.params
odds_ratios = params.apply(np.exp)
print("Odds ratios:\n", odds_ratios)
```

1. Explain what an odds ratio of, say, 1.05 for `monthly_charges` means.  
2. If `tenure` has odds ratio 0.97, how do odds of churn change per extra month?  
3. How would you explain odds ratios to a non-technical stakeholder?

---

### Case Study 3 – Adjusting the Decision Threshold

By default, we classify using threshold 0.5. Let's change it:

```python
from sklearn.metrics import confusion_matrix

y_proba = model.predict_proba(X_test)[:, 1]

for thr in [0.3, 0.5, 0.7]:
    y_pred_thr = (y_proba >= thr).astype(int)
    cm = confusion_matrix(y_test, y_pred_thr)
    print(f"Threshold {thr}")
    print(cm, "\n")
```

1. How does lowering the threshold affect **recall** for churners?  
2. How does it affect **precision**?  
3. In what business situation would you prefer high recall over precision (or vice-versa)?

---

### Case Study 4 – ROC Curve and AUC

```python
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

fpr, tpr, thr = roc_curve(y_test, y_proba)
auc = roc_auc_score(y_test, y_proba)

plt.plot(fpr, tpr, label=f"AUC = {auc:.3f}")
plt.plot([0, 0, 1], [0, 1, 1], linestyle="--")  # idealized step
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
```

1. Interpret an AUC of, say, 0.80.  
2. Why is ROC/AUC less sensitive to class imbalance than accuracy?  
3. What would an AUC close to 0.5 indicate?

---

### Case Study 5 – Credit Default Modeling

**Context**  
We want to model probability of **default** using:

- `income`  
- `loan_amount`  
- `age`

#### 💻 Python Skeleton

```python
np.random.seed(1)
n = 1500
income = np.random.normal(4000, 800, n)
loan_amount = np.random.normal(15000, 3000, n)
age = np.random.normal(40, 8, n)

logit = -5 + 0.0001*loan_amount - 0.00005*income - 0.02*age
p = 1 / (1 + np.exp(-logit))
default = (np.random.rand(n) < p).astype(int)

df = pd.DataFrame({
    "income": income,
    "loan_amount": loan_amount,
    "age": age,
    "default": default
})
```

#### 🧮 Questions

1. Based on the signs of the coefficients in the logit definition, how do `income`, `loan_amount`, and `age` affect default risk?  
2. Fit a logistic regression and compute odds ratios.  
3. Suggest how this model could be used in practice (e.g., risk-based pricing or credit approval).
