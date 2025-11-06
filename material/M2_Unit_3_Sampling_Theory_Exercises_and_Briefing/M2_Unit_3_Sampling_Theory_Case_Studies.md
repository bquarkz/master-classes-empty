# M2 Unit 3 – Sampling Theory  
## Case Study Exercises

---

## 🎯 Learning Goals

- Apply different sampling designs (simple, stratified, cluster, two-stage) in realistic scenarios.
- Understand how class imbalance interacts with sampling in machine learning problems.
- Use Python to simulate sampling schemes and inspect their impact on estimates and models.

---

### Case Study 1 – Stratified Sampling for Fraud Detection

**Context**  
You are building a fraud detection model for a bank. The dataset has **10,000 transactions**, of which **300 are fraudulent** and **9,700 are non-fraudulent**.  
You want to create a **training set of 4,000 observations**, preserving the class proportions using **stratified sampling**.

#### 🧮 Math Part

1. Explain why **simple random sampling (SRS)** might fail to give enough fraud examples in the training set when the classes are so imbalanced.
2. Let:
   - $N = 10{,}000$ (total),
   - $N_1 = 300$ (fraud),
   - $N_0 = 9{,}700$ (non-fraud),
   - desired training size $n = 4{,}000$.  

   Compute the stratified sample sizes:
   $$
   n_1 = \frac{N_1}{N} n, \quad
   n_0 = \frac{N_0}{N} n.
   $$
   Round them to whole numbers and report $n_1$ and $n_0$.
3. Suppose by mistake you only include **50 fraud cases** in the training set instead of the proportional amount.  
   Discuss qualitatively how this is likely to affect:
   - (a) **Recall** for the fraud class  
   - (b) **Precision** for the fraud class

#### 💻 Python Part

You receive a `DataFrame` `df` with a binary column `"is_fraud"`.

1. Use Python to create a stratified train/test split (train = 40%, test = 60%):

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Example: simulate the dataset
df = pd.DataFrame({"is_fraud": [0]*9700 + [1]*300})

train, test = train_test_split(
    df,
    test_size=0.6,
    stratify=df["is_fraud"],
    random_state=42
)

print("Train class proportions:")
print(train["is_fraud"].value_counts(normalize=True))
print("Test class proportions:")
print(test["is_fraud"].value_counts(normalize=True))
```

2. Repeat the split **without** using `stratify=`. Compare the class proportions in the training sets and explain what changes.
3. Reflect briefly: why can **stratified sampling by class** be crucial in imbalanced classification tasks?

---

### Case Study 2 – Cluster Sampling for Rural Household Surveys

**Context**  
A national statistics office wants to estimate the average household income in a rural region containing **100 villages**, each with **about 80 households** (so roughly 8,000 households).  

They compare:

- **Simple random sampling (SRS)** of individual households,
- **Cluster sampling**, where they sample whole villages.

They can afford to survey around **400 households**.

#### 🧮 Math Part

1. Under SRS, if they sample $n = 400$ households from $N = 8{,}000$, what is the selection probability for each household?
   $$
   P(\text{household selected}) = \frac{n}{N}.
   $$

2. Under cluster sampling, they randomly select $C = 5$ villages and interview **all households** in those villages.
   - What is $P(\text{village selected})$ for a given village?
   - Assuming 80 households per village, what is the approximate total sample size under this design?
3. Give one **practical advantage** (e.g. cost, logistics) and one **statistical disadvantage** (e.g. variance, representativeness) of the cluster sampling approach compared to SRS in this scenario.

#### 💻 Python Part (Simulation)

Simulate the population and compare SRS vs cluster sampling for estimating mean income:

```python
import numpy as np
import pandas as pd

np.random.seed(0)

# Create population
villages = np.repeat(np.arange(100), 80)
# base mean income per village
base_income = np.random.normal(3000, 200, size=100)
income = np.array([base_income[v] + np.random.normal(0, 150) for v in villages])

df = pd.DataFrame({"village": villages, "income": income})

# True population mean
pop_mean = df["income"].mean()

# SRS sample of 400 households
srs = df.sample(400, random_state=1)
srs_mean = srs["income"].mean()

# Cluster sample: choose 5 villages, take all households
chosen_villages = np.random.choice(df["village"].unique(), 5, replace=False)
cluster_sample = df[df["village"].isin(chosen_villages)]
cluster_mean = cluster_sample["income"].mean()

print("Population mean:", pop_mean)
print("SRS sample mean:", srs_mean)
print("Cluster sample mean:", cluster_mean)
```

Run this simulation a few times (changing the random seed) and describe how the SRS and cluster estimates behave relative to the true mean.

---

### Case Study 3 – Two-Stage Sampling in a Bank Network

**Context**  
A bank operates **60 branches**, each serving about **200 customers**. You want to estimate the average account balance across all customers using a **two-stage sampling design**:

1. **Stage 1**: randomly select 10 branches.  
2. **Stage 2**: within each selected branch, randomly select 30 customers.

#### 🧮 Math Part

1. What is the **expected total sample size** of customers under this design?
2. Compute the probability that a particular branch is selected at Stage 1.
3. Given a branch is selected, compute the probability that a specific customer in that branch is selected at Stage 2 (assume exactly 200 customers per branch).
4. Combine the results to find the **overall probability** that a specific customer in the entire network is included in the final sample.

#### 💻 Python Part

Simulate this two-stage sampling and estimate the mean balance:

```python
import numpy as np
import pandas as pd

np.random.seed(42)

branches = np.repeat(np.arange(60), 200)
balances = np.random.normal(5000, 800, size=len(branches))

df = pd.DataFrame({"branch": branches, "balance": balances})

# Stage 1: sample 10 branches
sel_branches = np.random.choice(df["branch"].unique(), 10, replace=False)

# Stage 2: sample 30 customers per selected branch
def sample_customers(group):
    return group.sample(30, random_state=42)

sample = (
    df[df["branch"].isin(sel_branches)]
    .groupby("branch", group_keys=False)
    .apply(sample_customers)
)

print("Sample size:", len(sample))
print("Sample mean balance:", sample["balance"].mean())
print("Population mean balance:", df["balance"].mean())
```

Compare the sample mean to the population mean and comment on the accuracy of the estimate.

---

### Case Study 4 – Bootstrapping a Sample Mean

**Context**  
You recorded **20 session durations** (in minutes) from users on a platform. The sample is small, and you do not want to rely too heavily on Normality assumptions. You decide to use **bootstrap resampling** to create a confidence interval for the mean session duration.

#### 🧮 Math Part

1. Describe the idea of **bootstrap resampling** in your own words. Mention:
   - resampling with replacement from the observed data,
   - approximating the sampling distribution of a statistic (like the mean),
   - using the spread of bootstrap statistics to build a confidence interval.

2. Explain why bootstrapping is especially useful when:
   - the sample size is small,
   - the underlying distribution might not be Normal.

#### 💻 Python Part

Assume you have the data in a NumPy array `x` of length 20. Implement a bootstrap for the mean:

```python
import numpy as np

def bootstrap_means(x, B=5000, random_state=0):
    rng = np.random.default_rng(random_state)
    n = len(x)
    means = []
    for _ in range(B):
        sample = rng.choice(x, size=n, replace=True)
        means.append(sample.mean())
    return np.array(means)

# Example usage:
x = np.array([5, 7, 9, 10, 12, 15, 18, 22, 25, 30,
              6, 8, 11, 13, 14, 16, 19, 21, 24, 28])

boot_means = bootstrap_means(x)
ci_low, ci_high = np.percentile(boot_means, [2.5, 97.5])
print("Bootstrap 95% CI for mean:", ci_low, ci_high)
```

Compare this bootstrap CI to a classical Normal-based CI and discuss any differences you see.

---

### Case Study 5 – Class Imbalance and Stratified Cross-Validation

**Context**  
You are training a classification model for a dataset with **5% positive** and **95% negative** examples. You want to evaluate the model using cross-validation in a fair way.

#### 🧮 Math / Conceptual Part

1. Explain the difference between:
   - **K-Fold Cross-Validation**
   - **Stratified K-Fold Cross-Validation**
2. Why can standard K-Fold be problematic for highly imbalanced datasets?
3. Why is **Stratified K-Fold** usually preferred in this context?

#### 💻 Python Part

Use scikit-learn to compare KFold and StratifiedKFold on an imbalanced dataset:

```python
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, make_scorer
import numpy as np

np.random.seed(0)

X = np.random.randn(1000, 5)
y = np.concatenate([np.zeros(950), np.ones(50)])

clf = LogisticRegression(max_iter=1000)
kf = KFold(n_splits=5, shuffle=True, random_state=0)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)

f1_kf = cross_val_score(clf, X, y, cv=kf, scoring=make_scorer(f1_score))
f1_skf = cross_val_score(clf, X, y, cv=skf, scoring=make_scorer(f1_score))

print("KFold F1 scores:", f1_kf)
print("StratifiedKFold F1 scores:", f1_skf)
print("Mean KFold F1:", f1_kf.mean())
print("Mean StratifiedKFold F1:", f1_skf.mean())
```

Compare the F1 scores and comment on which method gives more stable and realistic performance estimates for the minority class.
