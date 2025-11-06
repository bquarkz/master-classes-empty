# M2 Unit 9 – Poisson Regression  
## Fixation Exercises

---

## 🎯 Learning Goals

- Reinforce the intuition of Poisson models and link function.  
- Practice computing and interpreting rate ratios.  

---

## 🧮 Math Fixation

### 1. Poisson Mean and Variance

For a Poisson variable $Y \sim Poisson(\lambda)$:

1. Write $E[Y]$ and $Var[Y]$.  
2. If $\lambda = 4$, compute $P(Y = 0)$ and $P(Y = 2)$.  

---

### 2. Log-Link Model

Given $\log(\lambda) = 1 + 0.3x$, compute $\lambda$ when $x = 2$.  

---

### 3. Rate Ratios

If $\beta = 0.2$, compute $e^{\beta}$ and interpret it as an incidence rate ratio.  

---

### 4. Offset Concept

Explain why we include $\log(e_i)$ as an offset in Poisson regression when exposure differs between observations.  

---

### 5. Overdispersion Check

If sample mean = 2.5 and variance = 10.2, what does this imply about the Poisson assumption?  

---

## 💻 Python Fixation

### 1. Simple Poisson Fit

Simulate:

```python
import numpy as np
import statsmodels.api as sm

np.random.seed(0)
x = np.random.rand(100)*10
lam = np.exp(1 + 0.2*x)
y = np.random.poisson(lam)
X = sm.add_constant(x)
model = sm.GLM(y, X, family=sm.families.Poisson()).fit()
print(model.summary())
```

Interpret the coefficient for `x`.

---

### 2. Compute IRRs

Using the model above:

```python
import numpy as np
print(np.exp(model.params))
```

Interpret $IRR_x$.

---

### 3. Offset Example

Include an exposure offset:

```python
exposure = np.random.randint(1, 5, size=100)
model_offset = sm.GLM(y, X, offset=np.log(exposure), family=sm.families.Poisson()).fit()
```

Explain the role of the offset.

---

### 4. Overdispersion Detection

Compute variance and mean of residuals and compare:

```python
resid = model.resid_pearson
print("Overdispersion ratio:", (resid**2).sum() / model.df_resid)
```

If the ratio >> 1, what does that indicate?  

---

### 5. Negative Binomial Extension

Briefly note how to modify the Poisson model to use `sm.families.NegativeBinomial()` for overdispersed data.
