# M2 Unit 10 – Survival Analysis and Cox Regression  
## Math Briefing

---

## 🎯 Learning Goals

After this unit, you should be able to:

- Understand **time-to-event data** and **right censoring**.  
- Define and interpret **survival** and **hazard** functions.  
- Apply the **Kaplan–Meier estimator**.  
- Understand and fit the **Cox proportional hazards model**.  
- Interpret **hazard ratios** and covariate effects.

---

## 🧮 Key Mathematical Ideas

### 1. Survival Function

The **survival function** $S(t)$ is the probability of surviving beyond time $t$:

$$
S(t) = P(T > t) = 1 - F(t),
$$

where $F(t)$ is the cumulative distribution function (CDF) of event times.

### 2. Hazard Function

The **hazard function** $h(t)$ gives the instantaneous event rate at time $t$ (given survival until $t$):

$$
h(t) = \lim_{\Delta t \to 0} \frac{P(t \le T < t + \Delta t \mid T \ge t)}{\Delta t}.
$$

It represents the **risk** of event per unit time.

### 3. Relationship Between $S(t)$ and $h(t)$

They are linked by:

$$
S(t) = \exp\left(-\int_0^t h(u) \, du \right).
$$

---

### 4. Kaplan–Meier Estimator

Non-parametric estimator of survival function:

$$
\hat{S}(t) = \prod_{t_i \le t} \left(1 - \frac{d_i}{n_i}\right),
$$

where $d_i$ = number of events at $t_i$, and $n_i$ = number at risk just before $t_i$.

---

### 5. Cox Proportional Hazards Model

The **Cox model** relates hazard to covariates $X$ via:

$$
h(t|X) = h_0(t) \exp(\beta_1 X_1 + \cdots + \beta_p X_p),
$$

where:

- $h_0(t)$ is the **baseline hazard** (unspecified).  
- $\exp(\beta_j)$ is the **hazard ratio (HR)**: multiplicative change in hazard per unit increase in $X_j$.

Key assumption: **proportional hazards** — covariate effects are multiplicative and constant over time.

---

### 6. Interpreting the Hazard Ratio

If $\beta_j = 0.5$, then:

$$
e^{\beta_j} = 1.65
$$

→ The hazard is **65% higher** per unit increase in $X_j$.  
If $\beta_j = -0.7$, then $e^{\beta_j}=0.5$ → hazard is **halved**.

---

## 🤖 Why It Matters

Survival analysis applies beyond medicine — it’s about **time until event**:  
- Time until **machine failure**, **customer churn**, or **payment default**.  
- Cox models are widely used for **predicting risk** over time and identifying key drivers.

---

## 🔍 Where to Learn More

- “StatQuest: Survival Analysis”  
- “Cox Proportional Hazards Models in lifelines”  
- `lifelines` and `statsmodels` documentation

---

## 🧭 Key Terms

- Survival Function $S(t)$  
- Hazard Function $h(t)$  
- Censoring (Right-Censoring)  
- Kaplan–Meier Estimator  
- Cox Proportional Hazards Model  
- Hazard Ratio (HR)

---

**End of Math Briefing – M2 Unit 10**
