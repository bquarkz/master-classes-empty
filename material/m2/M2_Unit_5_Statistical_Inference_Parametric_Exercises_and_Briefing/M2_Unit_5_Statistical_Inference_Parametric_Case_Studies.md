# M2 Unit 5 – Statistical Inference (Parametric)  
## Case Study Exercises

---

## 🎯 Learning Goals

- Apply parametric inference to real-world problems.  
- Compute confidence intervals and hypothesis tests in Python.  
- Interpret p-values and results in context.

---

### Case Study 1 – One-Sample t-Test for Product Lifespan

**Context**  
A manufacturer claims that their batteries last **100 hours on average**. You collect a random sample of 20 batteries and find a sample mean of 96.5 hours with standard deviation 6.2 hours.

#### 🧮 Math Part

1. Set up hypotheses:  
   - $H_0: \mu = 100$  
   - $H_1: \mu < 100$  

2. Compute the t-statistic manually:  
   $$
   t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}.
   $$

3. With $n = 20$, $\bar{x} = 96.5$, $s = 6.2$, find $t$.  
4. Using a 5% significance level, decide whether to reject $H_0$.

#### 💻 Python Part

```python
from scipy import stats
import numpy as np

xbar, s, n = 96.5, 6.2, 20
mu0 = 100
t_stat = (xbar - mu0) / (s / np.sqrt(n))
p_value = stats.t.cdf(t_stat, df=n-1)
print("t =", t_stat, "p-value =", p_value)

# or directly from sample data
data = np.random.normal(96.5, 6.2, 20)
print(stats.ttest_1samp(data, popmean=100))
```

Interpret the result: is there strong evidence the mean is below 100?

---

### Case Study 2 – Two-Sample t-Test (Independent Samples)

**Context**  
A/B testing two website versions. You record time on site (in minutes) for 30 users each.

#### 💻 Python Part

Simulate and compare means:

```python
import numpy as np
from scipy import stats

np.random.seed(0)
A = np.random.normal(5, 1, 30)
B = np.random.normal(5.5, 1, 30)

t_stat, p_value = stats.ttest_ind(A, B, equal_var=True)
print("t =", t_stat, "p =", p_value)
```

#### 🧮 Questions

1. What are $H_0$ and $H_1$?  
2. Is there evidence that the new version (B) changes average time on site?  
3. Explain what the p-value tells you.

---

### Case Study 3 – Paired t-Test (Before/After)

**Context**  
A fitness app measures user step counts before and after a new motivational feature.

```python
import numpy as np
from scipy import stats

np.random.seed(1)
before = np.random.normal(8000, 500, 15)
after = before + np.random.normal(200, 300, 15)

t_stat, p_value = stats.ttest_rel(after, before)
print("Paired t-test:", t_stat, p_value)
```

#### 🧮 Discussion

1. What does the paired t-test check here?  
2. Interpret positive $t$ and low p-value in this context.  
3. How is this test different from the independent-sample test?

---

### Case Study 4 – F-Test for Comparing Variances

**Context**  
Two machines produce the same part. We suspect one machine has more variable output.

```python
import numpy as np

A = np.random.normal(10, 1.5, 25)
B = np.random.normal(10, 2.0, 25)

F = np.var(A, ddof=1) / np.var(B, ddof=1)
print("F statistic:", F)
```

1. Write hypotheses for comparing variances.  
2. How can you decide whether this F value is significant (using `scipy.stats.f`)?  
3. What does it mean if F >> 1?

---

### Case Study 5 – One-Way ANOVA

**Context**  
Three fertilizers (A, B, C) are tested for average crop yield (kg).

```python
import numpy as np
from scipy import stats

np.random.seed(0)
A = np.random.normal(30, 2, 15)
B = np.random.normal(32, 2, 15)
C = np.random.normal(33, 2, 15)

F, p = stats.f_oneway(A, B, C)
print("F =", F, "p =", p)
```

1. Write $H_0$: all group means equal.  
2. Interpret the p-value.  
3. What next step could you take if $H_0$ is rejected (e.g. Tukey’s test)?
