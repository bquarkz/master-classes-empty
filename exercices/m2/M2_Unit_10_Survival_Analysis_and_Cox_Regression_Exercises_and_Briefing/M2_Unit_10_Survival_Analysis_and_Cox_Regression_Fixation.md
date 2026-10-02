# M2 Unit 10 – Survival Analysis and Cox Regression  
## Fixation Exercises

---

## 🎯 Learning Goals

- Reinforce core ideas: survival, hazard, and censoring.  
- Practice interpreting hazard ratios.  

---

## 🧮 Math Fixation

### 1. Survival vs Hazard

Explain the conceptual difference between $S(t)$ and $h(t)$.  

### 2. Kaplan–Meier Step

Given $n_i = 10$ at risk and $d_i = 2$ events at $t_i$, compute the survival step $1 - d_i / n_i$.  

### 3. Hazard Ratio Interpretation

If $HR = 1.5$, how much higher is the risk?  
If $HR = 0.7$, how much lower is the risk?  

### 4. Censoring

Explain what right-censoring means and give one real-world example.

---

## 💻 Python Fixation

### 1. Kaplan–Meier Curve

Simulate survival data and plot $S(t)$ using `lifelines.KaplanMeierFitter`.  

### 2. Cox Model Fit

Fit a Cox model using `lifelines.CoxPHFitter` and interpret coefficients.  

### 3. Hazard Ratios

Extract hazard ratios via:

```python
import numpy as np
np.exp(cph.params_)
```

Interpret their meaning.
