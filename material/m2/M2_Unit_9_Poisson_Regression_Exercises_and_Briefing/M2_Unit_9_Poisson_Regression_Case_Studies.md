# M2 Unit 9 – Poisson Regression  
## Case Study Exercises

---

## 🎯 Learning Goals

- Model count data with Poisson regression.  
- Interpret coefficients and incidence rate ratios.  
- Evaluate model fit and detect overdispersion.

---

### Case Study 1 – Call Center Inbound Calls

**Context**  
A call center records the number of calls per hour (`calls`) along with `num_agents` (staff) and `hour_of_day`.

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm

np.random.seed(0)
n = 200
num_agents = np.random.randint(5, 15, n)
hour = np.random.randint(0, 24, n)
lam = np.exp(1 + 0.08*num_agents - 0.02*(hour - 12)**2 / 100)
calls = np.random.poisson(lam)

df = pd.DataFrame({"calls": calls, "num_agents": num_agents, "hour": hour})

X = sm.add_constant(df[["num_agents", "hour"]])
model = sm.GLM(df["calls"], X, family=sm.families.Poisson()).fit()
print(model.summary())
```

#### 🧮 Questions

1. Interpret the sign of `num_agents`.  
2. What does a coefficient of 0.08 mean in terms of rate ratio?  
3. How might `hour` represent non-linear effects (e.g., busy vs quiet hours)?

---

### Case Study 2 – Bike Rental Counts

**Context**  
A city records daily bike rentals as a function of temperature and rainfall.

```python
np.random.seed(1)
n = 300
temp = np.random.normal(20, 5, n)
rain = np.random.binomial(1, 0.3, n)
lam = np.exp(2 + 0.1*temp - 0.5*rain)
rentals = np.random.poisson(lam)

df = pd.DataFrame({"rentals": rentals, "temp": temp, "rain": rain})
X = sm.add_constant(df[["temp", "rain"]])
model = sm.GLM(df["rentals"], X, family=sm.families.Poisson()).fit()
print(model.summary())
```

1. Interpret coefficients for `temp` and `rain`.  
2. Compute and interpret `exp(β)` for each variable.  
3. What does the negative coefficient for rain indicate?

---

### Case Study 3 – Accidents by Road Segment

**Context**  
We record number of accidents per road segment, along with `traffic_volume` and `speed_limit`.

```python
np.random.seed(2)
n = 250
traffic = np.random.normal(2000, 400, n)
speed = np.random.normal(60, 10, n)
lam = np.exp(-5 + 0.0005*traffic + 0.03*speed)
accidents = np.random.poisson(lam)
df = pd.DataFrame({"accidents": accidents, "traffic": traffic, "speed": speed})
```

Fit a Poisson regression and compute **Incidence Rate Ratios**:

```python
X = sm.add_constant(df[["traffic", "speed"]])
model = sm.GLM(df["accidents"], X, family=sm.families.Poisson()).fit()
print(np.exp(model.params))
```

Interpret the IRRs.

---

### Case Study 4 – Hospital Admissions (Offset Example)

**Context**  
Different hospitals have different patient volumes. We model the number of daily admissions controlling for hospital size (offset).

```python
np.random.seed(3)
n = 100
beds = np.random.randint(50, 500, n)
region_score = np.random.normal(0, 1, n)
lam = np.exp(1 + 0.002*beds + 0.3*region_score)
adm = np.random.poisson(lam)

df = pd.DataFrame({"admissions": adm, "beds": beds, "region_score": region_score})

df["log_beds"] = np.log(df["beds"])
X = sm.add_constant(df[["region_score"]])
model = sm.GLM(df["admissions"], X, offset=df["log_beds"], family=sm.families.Poisson()).fit()
print(model.summary())
```

1. Why use an offset for `beds`?  
2. Interpret `region_score`.  
3. What would happen if we omitted the offset?

---

### Case Study 5 – Checking Overdispersion

**Context**  
You suspect overdispersion (variance > mean) in a Poisson model.

```python
mean_calls = df["admissions"].mean()
var_calls = df["admissions"].var()
print("Mean:", mean_calls, "Variance:", var_calls)
```

1. How can you detect overdispersion numerically or visually?  
2. Which model can replace Poisson if overdispersion is present (name it)?
