# M2 Unit 5 – Statistical Inference (Parametric)  
## Fixation Exercises

---

## 🎯 Learning Goals

- Strengthen conceptual and computational understanding of parametric inference.  
- Practice manual calculation and Python testing for means, variances, and differences.  

---

## 🧮 Math Fixation

### 1. Compute a t-Statistic

Given $n = 16$, $\bar{x} = 48.5$, $s = 4.0$, test $H_0: \mu = 50$.

1. Compute the t-statistic.  
2. With significance $\alpha = 0.05$, do we reject $H_0$ (two-tailed)?  

---

### 2. Confidence Interval for a Mean

A sample of 25 gives $\bar{x} = 75$, $s = 5$.  
Find a 95% confidence interval for $\mu$ using the t-distribution.  

---

### 3. Identify Test Type

Decide which test (Z, t, paired t, F, ANOVA) applies to:

1. Comparing weights of two unrelated groups.  
2. Testing improvement before/after training.  
3. Comparing 4 treatment means.  
4. Testing if population mean = known value.

---

### 4. Interpretation of p-Value

Explain what a **p-value = 0.03** means in the context of hypothesis testing at $\alpha = 0.05$.  

---

### 5. Type I vs Type II Errors

Define each error and describe what could cause them in an A/B test example.

---

### 6. Confidence and Significance

Explain how **confidence level** (e.g. 95%) relates to **significance level** ($\alpha = 0.05$).  

---

## 💻 Python Fixation

### 1. One-Sample t-Test

```python
from scipy import stats
import numpy as np

data = np.random.normal(50, 5, 30)
print(stats.ttest_1samp(data, popmean=52))
```

Interpret whether the sample provides evidence against $H_0: \mu = 52$.

---

### 2. Independent t-Test

Simulate two groups (A, B) and compare means:

```python
A = np.random.normal(10, 2, 20)
B = np.random.normal(11, 2, 20)
from scipy import stats
print(stats.ttest_ind(A, B))
```

---

### 3. Paired t-Test

```python
import numpy as np
from scipy import stats

before = np.random.normal(10, 1, 10)
after = before + np.random.normal(1, 1, 10)
print(stats.ttest_rel(after, before))
```

Interpret the sign of the t-value.

---

### 4. F-Test for Variance Ratio

Compute $F = s_1^2 / s_2^2$ and compare to critical values using:

```python
from scipy.stats import f
F = 2.5
df1, df2 = 24, 24
p = 1 - f.cdf(F, df1, df2)
print("p =", p)
```

---

### 5. One-Way ANOVA

Generate 3 groups and test equality of means using `stats.f_oneway`.

---

### 6. Confidence Interval via Python

Compute a 95% CI for a sample mean using:

```python
import numpy as np
from scipy import stats

x = np.random.normal(100, 10, 30)
mean, se = np.mean(x), stats.sem(x)
ci = stats.t.interval(0.95, len(x)-1, loc=mean, scale=se)
print(ci)
```

Interpret the interval.
