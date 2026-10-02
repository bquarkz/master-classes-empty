# M2 Unit 6 – Statistical Inference (Non-Parametric)  
## Fixation Exercises

---

## 🎯 Learning Goals

- Reinforce when to use each non-parametric test.  
- Practice Python implementations for quick rank-based analysis.  

---

## 🧮 Math Fixation

### 1. When to Use Non-Parametric Tests

Explain two cases where a non-parametric test is preferred over a parametric one.

---

### 2. Identify the Test

Choose the right test for each situation:

| Scenario | Appropriate Test |
|-----------|------------------|
| Comparing satisfaction scores (1–5) between two independent groups | ? |
| Testing improvement in stress levels before/after therapy | ? |
| Comparing 3 treatment groups with non-normal data | ? |
| Checking if gender and drink preference are related | ? |
| Measuring monotonic correlation between two ranked variables | ? |

---

### 3. Mann–Whitney U

Two independent samples have $n_1 = 8$, $n_2 = 10$. What does a very small U (close to 0) imply about the difference between groups?

---

### 4. Wilcoxon Logic

Explain what it means if the **sum of positive ranks** ≈ **sum of negative ranks** in a Wilcoxon test.

---

### 5. Kruskal–Wallis and Follow-up

If Kruskal–Wallis test rejects $H_0$, what’s the next analysis step?

---

### 6. Spearman Correlation

Given Spearman $\rho_s = -0.85$, describe the relationship between the two variables.

---

### 7. Chi-Square Expected Counts

In a 2x2 table with 60 males and 40 females, total 100, and 50 prefer tea, what is the expected count of males who prefer tea under independence?

---

## 💻 Python Fixation

### 1. Mann–Whitney

```python
from scipy import stats
A = [10, 12, 9, 11, 13, 10]
B = [8, 7, 9, 6, 8, 7]
print(stats.mannwhitneyu(A, B))
```

Interpret the p-value.

---

### 2. Wilcoxon

Simulate two paired samples (before/after) and perform Wilcoxon signed-rank test.

---

### 3. Kruskal–Wallis

Generate three groups of non-normal data and run `stats.kruskal`.

---

### 4. Spearman

Compute Spearman correlation between two NumPy arrays `x` and `y` with `stats.spearmanr`.

---

### 5. Chi-Square

Build a contingency table manually and use `chi2_contingency` to check association between two categorical variables.

---

### 6. Ranking Practice

Use `scipy.stats.rankdata` on `[50, 10, 30, 10, 90]` and print the ranks. Explain how ties are handled.
