# M2 Unit 9 – Poisson Regression  
## Math Briefing

---

## 🎯 Learning Goals

After this unit, you should be able to:

- Understand when to use **Poisson regression** for modeling count data.  
- Explain the **Poisson distribution** and its assumptions.  
- Derive and interpret the **log-linear model**.  
- Interpret coefficients as **rate ratios** (Incidence Rate Ratios – IRRs).  
- Implement Poisson regression in Python with `statsmodels`.

---

## 🧮 Key Mathematical Ideas

### 1. The Poisson Distribution

A random variable $Y$ follows a **Poisson distribution** if

$$
P(Y = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \dots
$$

where $\lambda > 0$ is both the **mean** and **variance** of the distribution:

$$
E[Y] = Var[Y] = \lambda.
$$

Poisson is typically used for **count data** — number of events per time, space, or unit.

---

### 2. Poisson Regression Model

We model the **expected count** $E[Y_i] = \lambda_i$ as:

$$
\log(\lambda_i) = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_k x_{ik}.
$$

or equivalently:

$$
\lambda_i = e^{\beta_0 + \beta_1 x_{i1} + \cdots + \beta_k x_{ik}}.
$$

This is a **Generalized Linear Model (GLM)** with:

- Random component: $Y_i \sim \text{Poisson}(\lambda_i)$  
- Link function: $g(\lambda_i) = \log(\lambda_i)$  
- Systematic component: linear predictor $\eta_i = X_i \beta$

---

### 3. Interpretation of Coefficients

Each $\beta_j$ represents the **log change** in expected count for a one-unit change in $x_j$, holding others constant.

Exponentiating gives the **Incidence Rate Ratio (IRR)**:

$$
IRR_j = e^{\beta_j}
$$

If $IRR_j = 1.2$, it means the rate increases by 20% for each unit increase in $x_j$.

---

### 4. Overdispersion

The Poisson assumption $Var(Y) = E(Y)$ is often too strict.  
If $Var(Y) > E(Y)$ (extra variation), the data are **overdispersed** — use **Negative Binomial regression** instead.

---

### 5. Offset Term

When counts are observed over varying exposures (e.g. time, population), we use an **offset** $\log(e_i)$:

$$
\log(\lambda_i) = \beta_0 + \beta_1 x_{i1} + \cdots + \log(e_i)
$$

This ensures rates are compared on a common scale.

---

## 🤖 Why It Matters

Poisson regression is widely used for:

- **Healthcare**: modeling number of visits, infections, deaths  
- **Marketing**: number of clicks, transactions  
- **Insurance**: number of claims  
- **Engineering**: defects per item or system failures per year

It’s a foundation for more complex models (Negative Binomial, Zero-Inflated Poisson, etc.).

---

## 🔍 Where to Learn More

- "StatQuest: Poisson and Log-Linear Models"  
- "GLMs in statsmodels"  
- "Overdispersion in count models"  

---

## 🧭 Key Terms

- Poisson Distribution, Rate Parameter $\lambda$  
- Log-Link Function  
- Maximum Likelihood Estimation  
- Incidence Rate Ratio (IRR)  
- Overdispersion  
- Offset Term  

---

**End of Math Briefing – M2 Unit 9**
