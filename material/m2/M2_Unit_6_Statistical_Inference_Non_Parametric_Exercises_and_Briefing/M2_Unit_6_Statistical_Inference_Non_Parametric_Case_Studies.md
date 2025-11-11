# M2 Unit 6 – Statistical Inference (Non-Parametric)  
## Case Study Exercises

---

## 🎯 Learning Goals

- Apply non-parametric inference techniques to real datasets.  
- Use rank-based and categorical tests in Python.  
- Interpret results when parametric assumptions fail.

---

### Case Study 1 – Mann–Whitney U Test: Comparing Two Independent Samples

**Context**  
You compare satisfaction scores (1–10) from two stores: Store A (n=12) and Store B (n=12). The data are ordinal and not normally distributed.

#### 💻 Python Part

```python
import numpy as np
from scipy import stats

A = [7,8,6,9,5,6,7,8,9,6,5,7]
B = [5,6,5,7,6,5,5,7,6,5,4,6]

U, p = stats.mannwhitneyu(A, B, alternative='two-sided')
print("U =", U, "p =", p)
```

#### 🧮 Questions

1. State $H_0$: both groups come from the same distribution.  
2. Interpret the p-value.  
3. Explain why Mann–Whitney is better than a t-test here.

---

### Case Study 2 – Wilcoxon Signed-Rank: Before vs After Treatment

**Context**  
A diet program measures participants’ weights before and after 6 weeks.

```python
import numpy as np
from scipy import stats

before = [82, 85, 90, 88, 91, 84, 87, 83]
after =  [80, 83, 88, 86, 89, 82, 85, 82]

stat, p = stats.wilcoxon(before, after)
print("Wilcoxon statistic:", stat, "p =", p)
```

#### 🧮 Discussion

1. What are $H_0$ and $H_1$?  
2. Interpret the sign of changes and p-value.  
3. Why is Wilcoxon more appropriate than a paired t-test?

---

### Case Study 3 – Kruskal–Wallis H: Comparing 3 Groups

**Context**  
Three different fertilizers (A, B, C) are used on 10 plants each. Yields (kg) are not normally distributed.

```python
import numpy as np
from scipy import stats

A = np.random.exponential(5, 10)
B = np.random.exponential(6, 10)
C = np.random.exponential(7, 10)

H, p = stats.kruskal(A, B, C)
print("H =", H, "p =", p)
```

1. What are $H_0$ and $H_1$?  
2. Interpret the result.  
3. If significant, what follow-up test could identify which groups differ?

---

### Case Study 4 – Spearman Rank Correlation

**Context**  
You measure website bounce rate (%) and average session time (min) for 15 websites.

```python
import numpy as np
from scipy import stats

bounce = np.random.uniform(30, 90, 15)
time = 100 - bounce + np.random.normal(0, 5, 15)

rho, p = stats.spearmanr(bounce, time)
print("Spearman rho =", rho, "p =", p)
```

1. Interpret the sign of $\rho_s$.  
2. What does a significant negative correlation mean in this context?

---

### Case Study 5 – Chi-Square Test of Independence

**Context**  
A survey asks 100 people about their **gender (M/F)** and **preference (Tea/Coffee)**.

```python
import numpy as np
from scipy.stats import chi2_contingency

table = np.array([[30, 20],
                  [10, 40]])  # rows: Male/Female; cols: Tea/Coffee

chi2, p, dof, exp = chi2_contingency(table)
print("Chi2 =", chi2, "p =", p)
print("Expected frequencies:\n", exp)
```

1. What are $H_0$ and $H_1$?  
2. Interpret the p-value.  
3. What does it mean if observed preferences differ greatly from expected values?
