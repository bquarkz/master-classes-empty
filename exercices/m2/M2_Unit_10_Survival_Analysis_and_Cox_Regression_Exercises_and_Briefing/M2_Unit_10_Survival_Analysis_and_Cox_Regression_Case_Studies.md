# M2 Unit 10 – Survival Analysis and Cox Regression  
## Case Study Exercises

---

## 🎯 Learning Goals

- Estimate and visualize survival curves.  
- Fit and interpret a Cox proportional hazards model.  
- Understand hazard ratios and time-dependent effects.

---

### Case Study 1 – Machine Failure Times

**Context**  
You have 100 machines, each observed until failure or censoring.

```python
import numpy as np
import pandas as pd
from lifelines import KaplanMeierFitter

np.random.seed(0)
n = 100
time = np.random.exponential(10, n)
event = np.random.binomial(1, 0.8, n)

kmf = KaplanMeierFitter()
kmf.fit(time, event_observed=event)
kmf.plot_survival_function()
```

#### 🧮 Questions

1. Interpret what the curve $S(t)$ shows.  
2. What does a steep drop in $S(t)$ mean?  
3. What does right-censoring mean in this context?
