# M2 Unit 8 – Binary Logistic Regression  
## Math Briefing

---

## 🎯 Learning Goals

After this unit, you should be able to:

- Understand the **logistic function** and how it links linear predictors to probabilities.  
- Interpret **odds**, **log-odds (logit)**, and logistic regression coefficients.  
- Recognize how logistic regression is fit via **maximum likelihood**.  
- Connect logistic regression to evaluation metrics such as **precision**, **recall**, **F1**, **ROC**, and **AUC**.

---

## 🧮 Key Mathematical Ideas (Plain Language)

### 1. Binary Outcomes

We model a binary response $Y \in \{0, 1\}$ (e.g. churn / no churn, default / no default, disease / no disease).  
For each observation with features $x$, we want to estimate

$$
P(Y = 1 \mid x).
$$

### 2. Logistic Function and Logit

Logistic regression assumes that the **log-odds** (logit) of $Y = 1$ is a linear function of the predictors:

$$
\text{logit}(p) = \log\left( \frac{p}{1 - p} \right) = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k,
$$

where $p = P(Y=1 \mid x)$.  

Solving for $p$ gives the **logistic function**:

$$
p = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k)}}.
$$

### 3. Odds and Interpretation of Coefficients

- **Odds** of an event are defined as
  $$
  \text{odds} = \frac{p}{1-p}.
  $$

- Each coefficient $\beta_j$ represents the change in **log-odds** when $x_j$ increases by 1 (holding other variables fixed).  
- Exponentiating, $e^{\beta_j}$ is the **odds ratio**: how many times the odds change for a one-unit increase in $x_j$.

### 4. Fitting the Model – Maximum Likelihood

Unlike linear regression, logistic regression does **not** minimize squared error.  
Instead, it uses **maximum likelihood estimation (MLE)**:

- For observed outcomes $y_i \in \{0,1\}$ with predicted probabilities $p_i$, the likelihood is
  $$
  L(\beta) = \prod_{i=1}^n p_i^{y_i} (1 - p_i)^{1 - y_i}.
  $$
- We usually maximize the **log-likelihood** numerically.

### 5. Decision Thresholds

The model outputs probabilities $p_i = P(Y_i = 1 \mid x_i)$.  
To make a binary decision, we choose a **cutoff** (often 0.5):

- Predict class 1 if $p_i \ge 0.5$, otherwise class 0.

For imbalanced or critical problems (fraud, medical diagnosis), different thresholds may be more appropriate.

---

## 🤖 Evaluation Metrics

Given predictions and true labels, key metrics are:

- **Accuracy**: proportion correctly classified.  
- **Precision**: among predicted positives, how many are actually positive.  
- **Recall (Sensitivity)**: among actual positives, how many are correctly predicted.  
- **F1-score**: harmonic mean of precision and recall.  
- **ROC curve**: plots TPR vs FPR across thresholds.  
- **AUC**: area under ROC; measures ranking quality.

---

## 🔍 Where to Learn More

- “StatQuest — Logistic Regression” (video)  
- “Interpreting logistic regression coefficients”  
- `sklearn.linear_model.LogisticRegression` docs  
- `statsmodels.discrete.discrete_model.Logit` docs  

---

## 🧭 Key Terms to Research

- Logistic Function, Sigmoid  
- Odds, Odds Ratio, Log-odds (Logit)  
- Maximum Likelihood Estimation  
- Decision Threshold, Calibration  
- Confusion Matrix, Precision, Recall, F1  
- ROC, AUC  

---

**End of Math Briefing – M2 Unit 8**
