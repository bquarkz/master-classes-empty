# M2 Unit 7 – Linear Regression (Part 2)  
## Math Briefing

---

## 🎯 Learning Goals

After this unit, you should be able to:

- Interpret coefficients, intercepts, and statistical significance in linear regression.  
- Understand $R^2$, adjusted $R^2$, and model diagnostics.  
- Perform hypothesis testing for regression parameters.  
- Detect multicollinearity, heteroscedasticity, and residual patterns.  

---

## 🧮 Key Mathematical Ideas

### 1. Recap: Simple Linear Regression

For a dependent variable $Y$ and one predictor $X$:

$$
Y_i = \beta_0 + \beta_1 X_i + \epsilon_i
$$

where $\epsilon_i$ are independent errors with mean 0 and variance $\sigma^2$.

---

### 2. Multiple Linear Regression

Extends to multiple predictors:

$$
Y = X\beta + \epsilon
$$

- $Y$ is $(n \times 1)$ vector of outcomes  
- $X$ is $(n \times p)$ matrix of predictors (including a column of 1s for intercept)  
- $\beta$ is $(p \times 1)$ vector of coefficients

The **least squares estimator** minimizes the residual sum of squares:

$$
\hat{\beta} = (X^T X)^{-1} X^T Y
$$

---

### 3. Interpretation of Coefficients

Each $\beta_j$ measures the change in $Y$ for a one-unit change in $X_j$, **holding other variables constant**.

---

### 4. Hypothesis Testing for Coefficients

For each coefficient $\beta_j$, we test:

$$
H_0: \beta_j = 0, \quad H_1: \beta_j \ne 0
$$

The **t-statistic** is:

$$
t_j = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}
$$

where $SE(\hat{\beta}_j)$ is the standard error of the estimate.  
If $|t_j| > t_{\alpha/2, n-p}$, reject $H_0$.

---

### 5. Model Significance – F-Test

Tests whether *at least one* predictor has a non-zero effect:

$$
F = \frac{(SSR / (p-1))}{(SSE / (n - p))}
$$

where:

- SSR = regression sum of squares  
- SSE = error sum of squares  

---

### 6. $R^2$ and Adjusted $R^2$

- $R^2$ measures proportion of variance explained:

$$
R^2 = 1 - \frac{SSE}{SST}
$$

- Adjusted $R^2$ corrects for number of predictors:

$$
R^2_{adj} = 1 - (1 - R^2)\frac{n-1}{n-p}
$$

---

### 7. Diagnostics

- **Residual plots** – detect non-linearity or heteroscedasticity.  
- **Variance Inflation Factor (VIF)** – checks multicollinearity.  
- **Normal Q-Q plot** – residual normality.  

---

## 🤖 Why It Matters

Regression diagnostics ensure your model’s predictions are meaningful and assumptions hold.  
In Data Science, this underpins model interpretability, fairness, and statistical reliability.  

---

## 🧭 Key Terms

- OLS Estimation  
- Coefficient Significance (t-test)  
- Model Fit ($R^2$, Adjusted $R^2$)  
- F-Test  
- VIF, Multicollinearity  
- Heteroscedasticity, Residual Analysis  

---

**End of Math Briefing – M2 Unit 7**
