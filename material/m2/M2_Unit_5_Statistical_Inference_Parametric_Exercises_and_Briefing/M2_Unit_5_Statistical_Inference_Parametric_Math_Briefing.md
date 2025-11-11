# M2 Unit 5 – Statistical Inference (Parametric)  
## Math Briefing

---

## 🎯 Learning Goals

After this unit, you should be able to:

- Understand the concepts of **point estimation**, **interval estimation**, and **hypothesis testing**.
- Recognize key parametric methods: **Z-test**, **t-test**, **F-test**, and **ANOVA**.
- Interpret **p-values**, **significance levels**, and **confidence intervals** correctly.
- Apply these concepts in Python using libraries like `scipy.stats` and `statsmodels`.

---

## 🧮 Key Mathematical Ideas (Plain Language)

### 1. Point Estimation

A **point estimator** provides a single best guess of a population parameter.

For example:

- Sample mean $\bar{x}$ estimates population mean $\mu$.
- Sample variance $s^2$ estimates population variance $\sigma^2$.

These are **statistics**, computed from data. Their expected value and variability determine their **bias** and **efficiency**.

### 2. Sampling Distributions and Standard Error

Each estimator (like $\bar{x}$) has its own sampling distribution.  
The **standard error (SE)** measures how much the estimator varies between samples:

$$
SE(\bar{x}) = \frac{s}{\sqrt{n}}.
$$

Larger samples → smaller SE → more precise estimates.

### 3. Confidence Intervals (CI)

A **confidence interval** provides a range of plausible values for a parameter.

For the mean (when population standard deviation is known):

$$
\bar{x} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}
$$

When $\sigma$ is unknown, use the **t-distribution** with $(n-1)$ degrees of freedom:

$$
\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}
$$

### 4. Hypothesis Testing

We test claims about population parameters by comparing data to the **null hypothesis ($H_0$)**.

Basic structure:

1. Set hypotheses ($H_0$, $H_1$).  
2. Choose significance level $\alpha$ (e.g. 0.05).  
3. Compute test statistic.  
4. Compute p-value or compare to critical value.  
5. Decide: reject or fail to reject $H_0$.

### 5. Common Tests

| Test | Purpose | Typical Formula | When to Use |
|------|----------|-----------------|--------------|
| **Z-test** | Test mean with known $\sigma$ | $Z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$ | Large samples or known variance |
| **t-test** | Test mean when $\sigma$ unknown | $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ | Small samples, unknown variance |
| **F-test / ANOVA** | Compare variances or multiple means | $F = \frac{s_1^2}{s_2^2}$ or variance ratio | Comparing group means |

---

## 📊 Example: One-Sample t-Test

We want to test if a sample mean differs from 50:

$$
H_0: \mu = 50, \quad H_1: \mu \ne 50.
$$

Compute:

$$
t = \frac{\bar{x} - 50}{s / \sqrt{n}}.
$$

Compare $|t|$ with $t_{\alpha/2, n-1}$ or find the p-value.

---

## 🤖 Why It Matters in Data Science / ML

Parametric inference is fundamental to:

- **A/B testing**: determining if conversion rates differ between designs.  
- **Model evaluation**: testing whether coefficients are significant.  
- **Experimental analysis**: comparing treatments or algorithms.  
- **Assumption checking**: confirming normality, homoscedasticity, independence.

Even advanced models (regressions, neural networks) rely on inference logic for model interpretation and uncertainty.

---

## 🔍 Where to Learn More

- “Understanding p-values” (StatQuest)  
- “Confidence Intervals and Significance Tests” (Khan Academy)  
- `scipy.stats.ttest_ind`, `statsmodels.stats.anova_lm`  
- “Central Limit Theorem explained visually”

---

## 🧭 Key Terms to Research

- Point Estimation, Standard Error  
- Confidence Interval, Margin of Error  
- Null Hypothesis ($H_0$), Alternative Hypothesis ($H_1$)  
- Test Statistic, p-value, Significance Level  
- Type I / Type II Errors  
- One-tailed vs Two-tailed tests  
- t-test, Z-test, F-test, ANOVA  

---

**End of Math Briefing – M2 Unit 5**
