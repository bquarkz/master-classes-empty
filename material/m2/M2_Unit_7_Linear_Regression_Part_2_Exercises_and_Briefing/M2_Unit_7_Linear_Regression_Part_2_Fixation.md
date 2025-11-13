# M2 Unit 7 – Linear Regression (Part 2)  
## Fixation Exercises

---

## 🎯 Learning Goals

- Reinforce regression inference and diagnostics.  
- Practice interpreting Python regression output.  

---

## 🧮 Math Fixation

### 1. t-Statistic for Coefficient

Given $\hat{\beta}_1 = 0.7$, $SE(\hat{\beta}_1) = 0.2$, test $H_0: \beta_1 = 0$ at $\alpha=0.05$.  

Compute $t = \frac{0.7}{0.2}$ and decide if significant for $df=20$.  

---

### 2. F-Test Interpretation

Explain in words what a significant F-test means in regression output.  

---

### 3. R² vs Adjusted R²

Why might adjusted $R^2$ decrease when adding more predictors?  

---

### 4. Multicollinearity

Define VIF and explain its meaning. What happens when VIF > 10?  

---

### 5. Residuals and Heteroscedasticity

What does it mean if residuals “fan out” as fitted values increase?  

---

## 💻 Python Fixation

### 1. Compute R²

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

np.random.seed(0)
X = np.random.rand(100, 1)*10
Y = 3 + 2*X + np.random.normal(0, 2, size=(100, 1))

model = LinearRegression().fit(X, Y)
print("R2 =", r2_score(Y, model.predict(X)))
```

---

### 2. t-Test for Coefficients in `statsmodels`

Fit a regression and interpret coefficient p-values from `model.summary()`.  

---

### 3. Confidence Intervals for Coefficients

Use `model.conf_int()` to get 95% intervals and interpret one that includes zero.  

---

### 4. VIF Check

Compute and interpret VIF using:

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
import numpy as np

X = np.random.rand(100, 3)
X = sm.add_constant(X)
[v for v in [variance_inflation_factor(X, i) for i in range(X.shape[1])]]
```

---

### 5. Residual Plot

Plot residuals and assess whether errors seem randomly distributed.  

---

### 6. QQ Plot

Generate residuals and create a Q-Q plot using:

```python
import scipy.stats as stats
import matplotlib.pyplot as plt

resid = model.resid
stats.probplot(resid, dist="norm", plot=plt)
plt.show()
```

Interpret whether residuals are approximately Normal.
