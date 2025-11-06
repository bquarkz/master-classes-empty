# M2 Unit 3 – Sampling Theory  
## Fixation Exercises

---

## 🎯 Learning Goals

- Reinforce the core definitions and formulas from **Sampling Theory**.
- Practice small, focused calculations involving sampling probabilities and proportional allocation.
- Write short Python snippets to connect sampling concepts to real code.

---

## 🧮 Math Fixation

### 1. SRS Selection Probability

A population has $N = 2{,}000$ units. You draw a simple random sample of $n = 100$ units without replacement.

1. Compute the probability that a particular unit is selected:
   $$
   P(\text{selected}) = \frac{n}{N}.
   $$
2. Interpret this probability in plain language.

---

### 2. Proportional Stratified Allocation

A population is divided into three strata:

- Stratum 1: $N_1 = 500$  
- Stratum 2: $N_2 = 1{,}000$  
- Stratum 3: $N_3 = 1{,}500$  

You want a total sample of $n = 200$ using **proportional stratified sampling**.

1. Compute $N = N_1 + N_2 + N_3$.  
2. Compute the stratum sample sizes:
   $$
   n_h = \frac{N_h}{N}\,n
   $$
   for $h = 1,2,3$.  
3. Check that $n_1 + n_2 + n_3 = 200$ (up to rounding).

---

### 3. Homogeneous Strata

Explain why, in stratified sampling, it is desirable that:

- Units **within** each stratum are similar to each other (homogeneous), but  
- Strata are **different from each other**.

Give a simple example of a good stratification variable (e.g. age group, income band, region) and explain your choice quickly.

---

### 4. Cluster vs Stratified Sampling

In your own words, describe the main difference between **stratified sampling** and **cluster sampling** regarding:

- How groups are formed  
- How we sample from those groups (within or entire groups)

Give an example for each where it would be more natural to use that design.

---

### 5. Class Imbalance and Accuracy

In a binary classification problem, the positive class has prevalence of **1%** (e.g. fraud).

1. Describe how a naive classifier that always predicts **negative** can still achieve 99% accuracy.  
2. Explain why accuracy is a misleading metric in this scenario.  
3. Suggest a more appropriate metric (e.g. recall, precision, F1-score) and briefly justify your choice.

---

### 6. Bootstrap Sample Size

You have a dataset of size $n = 50$ and you want to bootstrap the sample mean.

1. Why do we usually choose bootstrap sample size equal to $n$ (i.e. resample 50 values with replacement each time)?  
2. Conceptually, what could change if you used bootstrap samples of size 25 instead of 50?

---

## 💻 Python Fixation

### 1. Simple Random Sample from a DataFrame

Assume you have a `DataFrame` `df` with many rows.

Write a Python snippet that:

- Draws a simple random sample of **100 rows** from `df`,  
- Leaves the original `df` unchanged.

Hint: use `df.sample(...)`.

---

### 2. Stratified Train/Test Split by Label

Suppose `df` contains features in all columns except `"label"`, which is the target.

1. Use `train_test_split` to create a **70/30 stratified split** based on `"label"`.  
2. Print the class proportions in both train and test sets to verify stratification.

---

### 3. Manual K-Fold Index Split

Without using scikit-learn’s `KFold`, write Python code that:

- Takes `n = len(df)`  
- Produces a shuffled array of indices  
- Splits those indices into **5 folds** of (approximately) equal size

Hint: combine `np.random.permutation` and `np.array_split`.

---

### 4. Simple Bootstrap of a Mean in Python

Given:

```python
import numpy as np
x = np.array([5, 7, 9, 10, 12, 15, 18, 22, 25, 30])
```

Write a function `bootstrap_means(x, B=1000)` that:

- Draws `B` bootstrap samples (size `len(x)`, with replacement)  
- Computes the mean of each bootstrap sample  
- Returns the array of bootstrap means

Then compute the 2.5th and 97.5th percentiles of the bootstrap means to form a 95% interval.

---

### 5. Simulating Class Imbalance

1. Create a NumPy array `y` of length 1,000 that contains **950 zeros** and **50 ones**.  
2. Use `np.unique(y, return_counts=True)` to verify the distribution.  
3. (Optional) If you have `imblearn` installed, try oversampling the minority class using `RandomOverSampler` and print the new class counts.

---

### 6. Stratified K-Fold Skeleton

Write a small Python skeleton that sets up a `StratifiedKFold` with 5 splits and, for each split, prints the proportion of class 1 in the validation set.

```python
from sklearn.model_selection import StratifiedKFold
import numpy as np

X = np.random.randn(1000, 5)
y = np.concatenate([np.zeros(950), np.ones(50)])

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)

for fold, (_, val_idx) in enumerate(skf.split(X, y), start=1):
    y_val = y[val_idx]
    prop_pos = (y_val == 1).mean()
    print(f"Fold {fold}: proportion of class 1 in validation = {prop_pos:.3f}")
```

Check that each fold has roughly the same proportion of positives.
