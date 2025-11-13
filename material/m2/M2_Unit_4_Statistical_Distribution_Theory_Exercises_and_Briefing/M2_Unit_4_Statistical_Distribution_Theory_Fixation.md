# M2 Unit 4 – Statistical Distribution Theory  
## Fixation Exercises

---

## 🎯 Learning Goals

- Reinforce the basic properties of common probability distributions.
- Practice quick calculations and interpretations involving means, variances, and probabilities.
- Write small Python snippets to simulate and explore distributions.

---

## 🧮 Math Fixation

### 1. Binomial Basics

A random variable $X$ follows a Binomial distribution with parameters $n = 20$ and $p = 0.3$.

1. What is the interpretation of $n$ and $p$?  
2. Compute the mean $E[X]$ and variance $Var(X)$ using:
   $$
   E[X] = np, \quad Var(X) = np(1-p).
   $$

---

### 2. Poisson Mean and Variance

Let $Y \sim \text{Poisson}(\lambda)$ with $\lambda = 4$.

1. What are $E[Y]$ and $Var(Y)$?  
2. Interpret $\lambda$ in a real context (e.g. counts per hour).

---

### 3. Exponential Waiting Time

The waiting time $T$ between bus arrivals follows an Exponential distribution with rate $\lambda = 2$ (per hour).

1. What is the **mean waiting time** in hours?  
2. Convert this mean to minutes.  
3. Explain the **memoryless** property in simple terms.

---

### 4. Normal Standardization

Suppose $X \sim N(\mu = 50, \sigma = 5)$.

1. Write the formula for the standardized variable $Z$.  
2. Compute the $Z$-score for $X = 60$.  
3. Explain what a large positive $Z$-score means in this context.

---

### 5. Discrete vs Continuous

For each of the following examples, say whether a **discrete** or **continuous** distribution is more appropriate and name one candidate distribution:

1. Number of customers arriving in a shop in one hour.  
2. Time (in minutes) until the next earthquake in a region.  
3. Height (in cm) of adult males in a population.  
4. Number of defects on a manufactured item.

---

### 6. Lognormal vs Normal

1. Explain why a **Normal** distribution is not a good model for stock prices but can be a good model for **log-returns**.  
2. Briefly state why a **Lognormal** distribution is better suited for prices themselves.

---

## 💻 Python Fixation

### 1. Simulate a Binomial Sample

Use Python to simulate 10,000 realizations of a Binomial random variable with $n = 20$, $p = 0.3$:

```python
import numpy as np
from scipy.stats import binom

n, p = 20, 0.3
Nsim = 10000
samples = binom.rvs(n=n, p=p, size=Nsim)

print("Empirical mean:", samples.mean())
print("Empirical variance:", samples.var())
```

Compare the empirical mean and variance with the theoretical ones.

---

### 2. Simulate Poisson Counts

Simulate 10,000 realizations from a Poisson distribution with $\lambda = 4$ and compute the empirical mean and variance. Comment on how close they are to 4.

---

### 3. Exponential Waiting Times

Simulate 10,000 waiting times from an Exponential distribution with rate $\lambda = 2$:

```python
import numpy as np

lam = 2
Nsim = 10000
times = np.random.exponential(scale=1/lam, size=Nsim)
```

Compute the empirical mean and compare it to the theoretical mean $1/\lambda$.

---

### 4. Normal Histogram

Generate 5,000 observations from a Normal(0, 1) distribution and:

- Plot a histogram.  
- Compute the proportion of values between -1 and 1.  
- Compare this with the theoretical value (about 68%).

---

### 5. Simulate Lognormal Data

Simulate 5,000 Lognormal values using:

```python
import numpy as np

mu, sigma = 0.0, 0.5
lognormal_samples = np.random.lognormal(mean=mu, sigma=sigma, size=5000)
```

1. Plot a histogram of `lognormal_samples`.  
2. Compare visually with a histogram of `np.random.normal(mu, sigma, size=5000)`.  
3. Describe the main differences in shape (symmetry, skewness, support).

---

### 6. Quick Q-Q Plot Check

Write Python code that:

1. Simulates 1,000 values from a Normal(0, 1) distribution.  
2. Simulates 1,000 values from an Exponential(1) distribution.  
3. Creates Q-Q plots for both datasets against the Normal distribution.

Interpret which looks closer to a straight line and what that implies about Normality.
