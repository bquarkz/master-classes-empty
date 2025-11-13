# M2 Unit 7 – Linear Regression (Part 2)  
## Case Study Exercises

---

## 🎯 Learning Goals

- Apply hypothesis testing for regression parameters.  
- Evaluate regression diagnostics in Python.  
- Interpret model metrics and assumptions.  

---

### Case Study 1 – Coefficient Significance

**Context**  
A company models sales (`Y`) based on advertising spend (`X1`) and online engagement (`X2`).

```python
import statsmodels.api as sm
import numpy as np

np.random.seed(0)
X1 = np.random.normal(50, 10, 50)
X2 = np.random.normal(100, 20, 50)
Y = 5 + 0.8*X1 + 0.5*X2 + np.random.normal(0, 10, 50)

X = sm.add_constant(np.column_stack((X1, X2)))
model = sm.OLS(Y, X).fit()
print(model.summary())
```

#### 🧮 Discussion

1. Interpret the coefficients for `X1` and `X2`.  
2. What does the p-value for each predictor indicate?  
3. If `X2` has a high p-value, what might you conclude?

---

### Case Study 2 – F-Test for Model Significance

```python
print("F-statistic:", model.fvalue)
print("p-value:", model.f_pvalue)
```

1. Interpret what a significant F-test means.  
2. What does it tell us about the overall usefulness of the model?

---

### Case Study 3 – Residual Analysis

```python
import matplotlib.pyplot as plt

plt.scatter(model.fittedvalues, model.resid)
plt.axhline(0, color='red')
plt.xlabel("Fitted values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()
```

1. What should the residuals look like in a good model?  
2. How can patterns in residuals indicate problems like heteroscedasticity or non-linearity?

---

### Case Study 4 – Detecting Multicollinearity

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = [variance_inflation_factor(X, i) for i in range(X.shape[1])]
print(vif)
```

1. What is an acceptable VIF value?  
2. What does a high VIF indicate?  
3. How can we fix multicollinearity?

---

### Case Study 5 – Confidence Intervals for Coefficients

```python
print(model.conf_int())
```

1. Interpret a confidence interval that crosses zero.  
2. How does this relate to hypothesis testing on coefficients?  
3. When would you remove a variable based on CI results?
