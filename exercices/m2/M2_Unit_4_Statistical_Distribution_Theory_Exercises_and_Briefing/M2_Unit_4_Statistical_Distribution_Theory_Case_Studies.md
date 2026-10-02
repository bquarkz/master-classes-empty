# M2 Unit 4 – Statistical Distribution Theory  
## Case Study Exercises

---

## 🎯 Learning Goals

- Distinguish between discrete and continuous probability distributions.
- Decide when to use Binomial, Poisson, Exponential, Normal, and Lognormal models.
- Use Python to simulate distributions and compare theoretical expectations with empirical behavior.

---

### Case Study 1 – Choosing Between Binomial and Poisson

**Context**  
An insurance company tracks the number of claims filed in a month by a group of policyholders. Each policyholder either files a claim or not in a given month.

#### 🧮 Math Part

1. Explain when a **Binomial** model is appropriate:
   - What are the roles of $n$ (number of trials) and $p$ (probability of success)?  
   - What does a "success" represent here?

2. Explain when a **Poisson** model is appropriate:
   - How does the rate $\lambda$ relate to the average number of events in an interval?  
   - Why is Poisson often used for counts over time or space?

3. Suppose there are $n = 1{,}000$ policyholders, and each has a small probability $p = 0.01$ of filing a claim in a month.  
   - Compute the Binomial mean $E[X] = np$.  
   - Explain why a Poisson approximation with $\lambda = np$ may be reasonable in this case.

#### 💻 Python Part

Simulate and compare Binomial and Poisson counts:

```python
import numpy as np
from scipy.stats import binom, poisson

n = 1000
p = 0.01
lam = n * p
Nsim = 10000

binom_samples = binom.rvs(n=n, p=p, size=Nsim)
pois_samples = poisson.rvs(mu=lam, size=Nsim)

print("Empirical mean Binomial:", binom_samples.mean())
print("Empirical mean Poisson:", pois_samples.mean())
```

1. Plot histograms of `binom_samples` and `pois_samples` (optionally on top of each other) and comment on how similar they look.  
2. Discuss when this Poisson approximation could break down (e.g. larger $p$ or small $n$).

---

### Case Study 2 – Exponential Inter-Arrival Times in a Call Center

**Context**  
Calls arrive at a call center at an average rate of **6 calls per hour**. The number of calls per hour is modeled as a Poisson random variable with rate $\lambda = 6$. Under this model, the **waiting time** between calls follows an Exponential distribution with the same rate $\lambda$.

#### 🧮 Math Part

1. Write down the Exponential density for the waiting time $T$ between calls with rate $\lambda = 6$ (per hour):
   $$
   f(t) = \lambda e^{-\lambda t}, \quad t \ge 0.
   $$

2. Compute the **expected waiting time** between calls in hours and in minutes.

3. What is the probability that the waiting time is **less than 5 minutes**?  
   (Hint: convert 5 minutes to hours and use the Exponential CDF.)

#### 💻 Python Part

Simulate a large number of inter-arrival times and estimate the probabilities:

```python
import numpy as np

lam = 6  # per hour
scale = 1 / lam  # mean in hours

Nsim = 100000
times = np.random.exponential(scale=scale, size=Nsim)  # in hours

# Convert to minutes
times_min = times * 60

# Empirical probability of waiting less than 5 minutes
p_empirical = np.mean(times_min < 5)
print("Empirical P(T < 5 min):", p_empirical)
```

Compare this empirical probability with your theoretical result. Comment on the similarity.

---

### Case Study 3 – Normal Distribution and Exam Scores

**Context**  
Exam scores in a large class are approximately Normal with mean $\mu = 70$ and standard deviation $\sigma = 10$. Scores range from 0 to 100.

#### 🧮 Math Part

1. Using the **68–95–99.7 rule**, what interval approximately covers 95% of the scores?  
   (That is, $\mu \pm 2\sigma$.)

2. Compute the **probability** that a randomly chosen student scores above 85.  
   - Express 85 as a $Z$-score.  
   - Use the Normal CDF (tables or software) to find $P(X > 85)$.

3. Interpret this probability in plain language (e.g. "about X% of students score above 85").

#### 💻 Python Part

Simulate scores and compare empirical to theoretical probabilities:

```python
import numpy as np
from scipy.stats import norm

mu, sigma = 70, 10
Nsim = 100000
scores = np.random.normal(mu, sigma, size=Nsim)

# empirical probability of score > 85
p_empirical = np.mean(scores > 85)

# theoretical probability
p_theoretical = 1 - norm.cdf(85, loc=mu, scale=sigma)

print("Empirical P(X > 85):", p_empirical)
print("Theoretical P(X > 85):", p_theoretical)
```

Compare the two values and explain why they should be close.

---

### Case Study 4 – Lognormal Model for Prices

**Context**  
Daily stock prices are often modeled as **Lognormal**, which means that **log-returns** follow a Normal distribution. Suppose the daily log-return $R = \log(P_t / P_{t-1})$ is modeled as Normal with mean $\mu_R$ and standard deviation $\sigma_R$.

#### 🧮 Math Part

1. Explain in words what it means for a price $P$ to be Lognormal.  
   (Hint: $\log(P)$ is Normal.)

2. Give two reasons why Lognormal is more realistic than Normal for prices:
   - Support (values must be positive).  
   - Price changes are often **multiplicative** rather than additive.

3. If $R \sim N(\mu_R, \sigma_R^2)$, what is the expression for the price at time $t$ in terms of $P_0$ and cumulative returns? (You can write this in words or as a product involving exponentials.)

#### 💻 Python Part

Simulate one possible price path over 252 trading days (roughly one year):

```python
import numpy as np

np.random.seed(0)
mu_R = 0.0005   # mean daily log-return
sigma_R = 0.01  # std of daily log-return
N = 252
log_returns = np.random.normal(mu_R, sigma_R, size=N)

prices = 100 * np.exp(np.cumsum(log_returns))  # start at 100

print("First 5 prices:", prices[:5])
print("Last price:", prices[-1])
```

1. Plot the price path over time (if you are in a notebook with plotting).  
2. Also plot a histogram of `log_returns` to see if it is approximately Normal.

---

### Case Study 5 – Q-Q Plot for Checking Normality of Residuals

**Context**  
You fit a linear regression model and obtain the **residuals** (differences between observed and predicted values). One of the key assumptions of linear regression is that these residuals are approximately Normally distributed.

#### 🧮 Math / Conceptual Part

1. Explain what a **Q-Q plot** is comparing when we check Normality.  
2. Describe what you expect to see in a Q-Q plot if the data are approximately Normal.  
3. Describe patterns that indicate strong deviations from Normality (e.g. heavy tails, skewness).

#### 💻 Python Part

Generate a Q-Q plot for Normal and non-Normal data:

```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

np.random.seed(0)

normal_data = np.random.normal(size=500)
exp_data = np.random.exponential(size=500)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

stats.probplot(normal_data, dist="norm", plot=axes[0])
axes[0].set_title("Q-Q Plot: Normal data")

stats.probplot(exp_data, dist="norm", plot=axes[1])
axes[1].set_title("Q-Q Plot: Exponential data")

plt.tight_layout()
plt.show()
```

Compare the two plots and describe the differences you see. Which one looks more like a straight line? Why?
