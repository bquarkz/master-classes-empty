# M2 Unit 8 – Binary Logistic Regression  
## Fixation Exercises

---

## 🎯 Learning Goals

- Fix core intuition on odds, log-odds, and thresholds.  
- Practice basic logistic regression workflows in Python.  

---

## 🧮 Math Fixation

### 1. Odds and Probabilities

1. If $P(Y=1) = 0.8$, compute the odds.  
2. If odds are 3 to 1 in favor of an event, what is the corresponding probability?  

---

### 2. Logit and Coefficients

Given

$$
\text{logit}(p) = -1 + 0.4 x,
$$

1. Write $p(x)$ explicitly using the logistic function.  
2. What happens to $p$ as $x$ increases?  

---

### 3. Odds Ratio Interpretation

If $\beta_1 = 0.7$, compute $e^{\beta_1}$ and interpret it as an odds ratio.  

---

### 4. Threshold Choice

Explain why using a default probability threshold of 0.5 can be problematic when:

- The positive class is rare (e.g. 1% fraud).  
- The cost of false negatives is very high.  

---

## 💻 Python Fixation

### 1. Fit a Simple Logistic Regression

Simulate:

```python
import numpy as np
from sklearn.linear_model import LogisticRegression

np.random.seed(0)
n = 500
x = np.random.randn(n)
logit = -0.5 + 1.2*x
p = 1 / (1 + np.exp(-logit))
y = (np.random.rand(n) < p).astype(int)

X = x.reshape(-1, 1)
model = LogisticRegression()
model.fit(X, y)
print("Coef:", model.coef_, "Intercept:", model.intercept_)
```

Compare the estimated coefficient and intercept to the true values.

---

### 2. Confusion Matrix and Report

Add:

```python
from sklearn.metrics import confusion_matrix, classification_report
y_pred = model.predict(X)
print(confusion_matrix(y, y_pred))
print(classification_report(y, y_pred))
```

Identify precision and recall.

---

### 3. Changing Threshold

Use `predict_proba` and experiment with thresholds 0.3, 0.5, 0.7. Observe changes in confusion matrix.

---

### 4. Odds Ratios with statsmodels

Fit the same model with `statsmodels` and compute `np.exp(params)` to obtain odds ratios.

---

### 5. ROC and AUC Quick Check

Compute ROC AUC using `roc_auc_score(y, model.predict_proba(X)[:,1])` and interpret.

---

### 6. Feature Scaling Thought

Explain briefly whether logistic regression **requires** feature scaling and why scaling can still be useful (e.g., for optimization and interpretation).
