# M2 Unit 3 – Sampling Theory  
## Math Briefing

---

## 🎯 Learning Goals

After this unit, you should be able to:

- Understand what **population**, **sample**, and **sampling design** mean.
- Recognize the difference between **simple random sampling**, **stratified sampling**, and **cluster sampling**.
- Grasp the ideas of **sampling error** and **bootstrap resampling** at an intuitive level.
- Connect sampling choices to practical tasks in **machine learning** and **data analysis**.

---

## 🧮 Key Mathematical Ideas (Plain Language)

### Population vs Sample

- **Population**: the full set of items you care about (all customers, all transactions, all patients, etc.).  
- **Sample**: the smaller subset you actually observe and analyze.

Good sampling tries to ensure that the sample is **representative** of the population.

### Simple Random Sampling (SRS)

Every unit in the population has the **same probability** of being chosen.

If there are $N$ units in the population and you choose $n$ units at random (without replacement), each unit has probability

$$
P(\text{unit is selected}) = \frac{n}{N}.
$$

### Stratified Sampling

- The population is split into **homogeneous groups** (strata), such as age groups, income levels, or regions.
- Then you sample from **each stratum**, often proportionally to its size.

This improves representation of important sub-groups and usually gives **more precise estimates** than SRS if strata are well chosen.

### Cluster Sampling

- The population is divided into **clusters** (e.g. villages, schools, companies).
- Instead of sampling individuals across the whole population, you randomly choose some clusters and observe **all** (or many) units inside them.

Cluster sampling can be cheaper and more practical, but may have **larger variance** than SRS if clusters are internally heterogeneous.

### Sampling Error

Because we only see a **sample**, estimates (like the sample mean) are not exactly equal to true population values.

- **Sample mean**:
  $$
  \bar{x} = \frac{1}{n}\sum_{i=1}^n x_i
  $$

- **Population mean** (usually unknown in practice):
  $$
  \mu = \frac{1}{N}\sum_{i=1}^N x_i
  $$

The difference $\bar{x} - \mu$ is part of the **sampling error**.

### Bootstrap Resampling

When we do not know the true sampling distribution, we can approximate it by:
- repeatedly **resampling with replacement** from the observed data,
- computing the statistic (e.g. mean) on each resample,
- using the variation among these bootstrap statistics to estimate **uncertainty** (e.g. confidence intervals).

---

## 📊 Light Touch on Equations

1. **Selection probability in SRS**

   $$
   P(\text{unit selected}) = \frac{n}{N}
   $$

2. **Proportional allocation in stratified sampling**

   Suppose we have $H$ strata, sizes $N_1, N_2, \dots, N_H$, total $N$.  
   For a total sample size $n$, proportional allocation gives stratum sample sizes

   $$
   n_h = \frac{N_h}{N}\,n, \quad h = 1,2,\dots,H.
   $$

3. **Standard Error idea (informal)**

   For a sample mean, a rough idea is:

   $$
   SE(\bar{x}) \approx \frac{\sigma}{\sqrt{n}},
   $$

   where $\sigma$ is the population standard deviation. In practice we estimate $\sigma$ from data.

---

## 🤖 Why It Matters in Data Science / ML

Sampling Theory is at the heart of:

- **Train/test splits** and **cross-validation**: we want each subset to be representative of the whole.
- Handling **class imbalance**: stratified sampling (e.g. by target class) ensures that minority classes are present in each split.
- **Survey data**, **A/B tests**, and **online experiments**: design matters for valid inference.
- **Bootstrap methods**: used for estimating uncertainty when analytic formulas are complex or assumptions are doubtful.

If sampling is biased or poorly designed, all downstream conclusions and ML models can be misleading, no matter how sophisticated the algorithms are.

---

## 🔍 Where to Learn More

Useful search terms and resources:

- "Simple random sampling vs stratified sampling vs cluster sampling"
- "Sampling error and standard error"
- "Bootstrap resampling explained (StatQuest)"
- "Khan Academy – sampling and surveys"
- "Cross-validation and stratification in machine learning"

---

## 🧭 Key Terms to Research

- Population, Sample, Sampling Frame  
- Simple Random Sampling (SRS)  
- Stratified Sampling, Strata  
- Cluster Sampling, Two-Stage Sampling  
- Sampling Error, Standard Error  
- Bootstrap, Resampling  
- Class Imbalance, Stratified Cross-Validation

---

**End of Math Briefing – M2 Unit 3**
