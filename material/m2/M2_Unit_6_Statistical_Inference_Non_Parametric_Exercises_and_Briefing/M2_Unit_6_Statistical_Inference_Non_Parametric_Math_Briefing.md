# M2 Unit 6 – Statistical Inference (Non-Parametric)  
## Math Briefing

---

## 🎯 Learning Goals

After this unit, you should be able to:

- Understand when **non-parametric** tests are needed instead of parametric ones.  
- Identify key non-parametric methods: **Mann-Whitney U**, **Wilcoxon signed-rank**, **Kruskal-Wallis**, **Spearman correlation**, and **Chi-square** tests.  
- Interpret test results and apply them using Python.  

---

## 🧮 Key Mathematical Ideas (Plain Language)

### 1. Why Non-Parametric Tests?

Parametric tests (like t-tests or ANOVA) assume data come from a **Normal distribution** and have **equal variances**.  
When these assumptions fail — or when data are **ordinal** (ranks) or have **outliers** — we use **non-parametric** tests.

These tests rely on **ranks** rather than raw values, making them robust and flexible.

---

### 2. Common Non-Parametric Tests

| Test | Parametric Equivalent | Data Type | Use Case |
|------|-----------------------|-----------|-----------|
| **Mann–Whitney U** | Independent t-test | Ordinal or non-normal continuous | Compare two independent groups |
| **Wilcoxon Signed-Rank** | Paired t-test | Ordinal or paired samples | Compare before/after or matched data |
| **Kruskal–Wallis H** | One-way ANOVA | Ordinal / non-normal continuous | Compare three or more groups |
| **Spearman Correlation** | Pearson correlation | Ordinal / non-linear relation | Measure monotonic association |
| **Chi-Square** | – | Categorical | Test association between categories |

---

### 3. Mann–Whitney U Test

Compares medians of two independent groups.

If sample sizes are $n_1$ and $n_2$, we rank all observations together, then compute the U statistic:

$$
U = n_1 n_2 + \frac{n_1(n_1 + 1)}{2} - R_1,
$$

where $R_1$ is the sum of ranks in group 1.  
The test checks whether the rank distributions differ significantly.

---

### 4. Wilcoxon Signed-Rank Test

Paired-sample alternative to the t-test.  
For paired observations $(x_i, y_i)$, compute differences $d_i = x_i - y_i$, ignore zeros, rank $|d_i|$, then sum ranks by sign.  
Tests if median difference is zero.

---

### 5. Kruskal–Wallis H Test

Generalizes Mann–Whitney to more than two groups.  
Ranks all data together, computes statistic:

$$
H = \frac{12}{N(N+1)} \sum_{i=1}^k n_i (\bar{R}_i - \bar{R})^2,
$$

where $\bar{R}_i$ is average rank in group i.  
Compared to chi-square distribution with $(k-1)$ degrees of freedom.

---

### 6. Spearman Rank Correlation

Measures monotonic (not necessarily linear) relationship between two variables.  
Computed as Pearson correlation of the **ranks**:

$$
\rho_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)},
$$

where $d_i$ is the rank difference for each pair.

---

### 7. Chi-Square Test for Independence

Tests whether two categorical variables are independent.  
Statistic:

$$
\chi^2 = \sum \frac{(O - E)^2}{E},
$$

where $O$ = observed counts, $E$ = expected counts under independence.

---

## 🤖 Why It Matters in Data Science / ML

Non-parametric methods are vital when:

- Data contain **outliers** or are **non-normal**.  
- You’re analyzing **ordinal ratings** (e.g., Likert scales).  
- Categorical relationships matter (Chi-square).  
- Robust statistics are needed for noisy real-world data.

Many ML feature-selection techniques rely on non-parametric correlations (e.g. Spearman, mutual information).

---

## 🔍 Where to Learn More

- "Non-parametric tests explained" (StatQuest)  
- "Mann–Whitney U vs t-test"  
- "Wilcoxon Signed-Rank Intuition"  
- "Kruskal–Wallis example in Python"  
- "Chi-square test for independence"  

---

## 🧭 Key Terms to Research

- Ranks, Ordinal Data  
- Mann–Whitney U, Wilcoxon Signed-Rank  
- Kruskal–Wallis H, Spearman ρ  
- Chi-Square Statistic  
- p-value interpretation  

---

**End of Math Briefing – M2 Unit 6**
