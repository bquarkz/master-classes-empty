# M2 Unit 4 – Statistical Distribution Theory  
## Math Briefing

---

## 🎯 Learning Goals

After this unit, you should be able to:

- Understand the difference between **discrete** and **continuous** probability distributions.
- Recognize common distributions: **Binomial**, **Poisson**, **Exponential**, **Normal**, and **Lognormal**.
- Interpret basic parameters such as **mean**, **variance**, and **rate** $\lambda$.
- Connect distribution choices to real-world data (counts, waiting times, measurements, prices).

---

## 🧮 Key Mathematical Ideas (Plain Language)

### Random Variables and Distributions

- A **random variable** is a quantity whose value is uncertain (e.g. number of calls in an hour, height of a person).
- A **distribution** describes how likely different values are.

We often distinguish:

- **Discrete distributions**: outcomes are counts or separated values (0, 1, 2, ...).  
- **Continuous distributions**: outcomes can vary over an interval (e.g. any real value in a range).

### Common Discrete Distributions

1. **Binomial**  
   - Models the number of *successes* in a fixed number $n$ of independent trials, with success probability $p$ each time.  
   - Example: number of heads in 10 coin flips.

   Probability mass function (PMF):
   $$
   P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}, \quad k = 0,1,\dots,n.
   $$

2. **Poisson**  
   - Models counts of events in a fixed interval of time or space when events occur at an average rate $\lambda$ and are roughly independent.  
   - Example: number of calls to a call center in an hour.

   PMF:
   $$
   P(X = k) = \frac{e^{-\lambda}\lambda^k}{k!}, \quad k = 0,1,2,\dots
   $$

### Common Continuous Distributions

1. **Exponential**  
   - Models **waiting times** between events in a Poisson process.  
   - Parameter $\lambda > 0$ is the rate (events per unit time).  
   - Density:
     $$
     f(t) = \lambda e^{-\lambda t}, \quad t \ge 0.
     $$
   - Mean waiting time is $1/\lambda$.  
   - Has the **memoryless** property: the future does not depend on the past waiting time.

2. **Normal (Gaussian)**  
   - Bell-shaped, continuous distribution often used for **measurement errors** or sums/averages of many small effects.  
   - Parameters: mean $\mu$ (center) and standard deviation $\sigma$ (spread).  
   - Many statistics are approximately Normal by the **Central Limit Theorem**.

3. **Lognormal**  
   - A random variable $X$ is Lognormal if $\log(X)$ is Normal.  
   - Models positive quantities with multiplicative growth, such as prices and incomes.

---

## 📊 Light Touch on Equations

1. **Mean and variance (examples)**

- For a Binomial($n,p$):
  $$
  E[X] = np, \quad Var(X) = np(1-p).
  $$
- For a Poisson($\lambda$):
  $$
  E[X] = \lambda, \quad Var(X) = \lambda.
  $$
- For Exponential($\lambda$):
  $$
  E[T] = \frac{1}{\lambda}, \quad Var(T) = \frac{1}{\lambda^2}.
  $$

2. **Standardization (Normal)**

To compare values from different Normal distributions, we often standardize:

$$
Z = \frac{X - \mu}{\sigma},
$$

where $Z$ follows a standard Normal distribution if $X$ is Normal with mean $\mu$ and standard deviation $\sigma$.

---

## 🤖 Why It Matters in Data Science / ML

Different data types naturally call for different distributions:

- **Counts** (number of events): Poisson, Binomial.  
- **Waiting times**: Exponential.  
- **Measurements / errors**: Normal.  
- **Positive skewed data** (prices, incomes): Lognormal, Gamma.

Choosing the right distribution helps to:

- Build better **probabilistic models** and **likelihood functions**.  
- Compute more accurate **p-values**, **confidence intervals**, and **prediction intervals**.  
- Understand the **assumptions** behind models like linear regression (Normal errors) or Poisson regression (Poisson counts).

---

## 🔍 Where to Learn More

Useful search terms and resources:

- "Binomial vs Poisson distribution intuition"
- "Exponential distribution waiting times and memoryless property"
- "Normal distribution and Central Limit Theorem"
- "Lognormal distribution and stock prices"
- "StatQuest: Poisson, Binomial, Normal, Exponential"

---

## 🧭 Key Terms to Research

- Probability mass function (PMF), Probability density function (PDF)  
- Binomial, Poisson, Exponential, Normal, Lognormal  
- Mean, Variance, Standard Deviation  
- Rate parameter $\lambda$  
- Central Limit Theorem (CLT)  
- Standardization, Z-scores  
- Tail probabilities, CDF (Cumulative Distribution Function)

---

**End of Math Briefing – M2 Unit 4**
