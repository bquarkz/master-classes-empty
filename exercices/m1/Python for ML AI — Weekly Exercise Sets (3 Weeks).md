# Python for ML/AI — Weekly Exercise Sets (3 Weeks)

Welcome! 👋 These exercises are designed for **beginners to intermediate learners**, including those **without a computer science background**. You will practice modern Python fundamentals in **Jupyter Notebooks**, building toward core ideas used in **Machine Learning (ML) and Artificial Intelligence (AI)**. The progression follows your course outline (CP01–CP10): from Python basics and data types, through control flow and functions, to decorators, error handling, dates/times, and functional programming (lambda/map).

## How to use these exercises

* Work inside Jupyter Notebooks (one notebook per week by default).
* **Some exercises explicitly ask for their own dedicated notebook** (so you can present results clearly).
* Add short **Markdown explanations** above each solution cell describing your approach.
* Prefer **clean, reusable functions** over copy‑paste code (I strongly recommend the use of a backend).
* **Unit tests** are encouraged but not required.
* Visualize where helpful (we could use `matplotlib`).

---

## 📅 Week 1 — Python Fundamentals & Data Structures

Focus: **CP01–CP05** (Intro, numbers & strings, collections, control flow, basic functions)

**Suggested main notebook:** `wk01_fundamentals.ipynb`

1. **Hello, AI! (Warm‑up)**
   Print a personalized greeting with today’s date/time. Use `datetime` and f‑strings.
   *Notebook:* main week notebook.

2. **Type Explorer**
   Create variables of types `int`, `float`, `bool`, `str`, and `complex`. Show their `type()` and basic operations (e.g., string slicing, numeric arithmetic).
   *Notebook:* main week notebook.

3. **String Lab: Cleaning & Counting**
   Given a paragraph, output: lowercased text, trimmed extra spaces, number of words, and count of vowels/consonants.
   *Notebook:* main week notebook.

4. **Control‑Flow Mini‑Calculator**
   Read two numbers and an operator (`+ - * /`). Validate input and compute the result using `if/elif/else`. Handle division by zero gracefully.
   *Notebook:* main week notebook.

5. **Lists 101: Stats & Slices**
   Create a list of 30 random integers in `[0, 100]`. Show: sorted ascending/descending, sum, mean, min, max, first 5, last 5, evens/odds.
   *Notebook:* main week notebook.

6. **Tuples vs Lists (Immutability Demo)**
   Demonstrate an attempted mutation on a tuple and capture the resulting exception. Explain when a tuple is preferable to a list.
   *Notebook:* main week notebook.

7. **Dictionaries as Tiny Databases**
   Maintain a `students` dictionary mapping names → list of grades. Implement functions to add a student, update grades, compute class average, and top‑N students.
   *Notebook:* main week notebook.

8. **Set Operations for NLP‑ish Tasks**
   Given two sets of words (e.g., from two short texts): compute intersection, union, difference; list unique vs common words.
   *Notebook:* main week notebook.

9. **FizzBuzz with a Twist**
   For numbers 1..75 print `Fizz` (×3), `Buzz` (×5), `FizzBuzz` (×15), else the number. Then, count how many of each label appeared.
   *Notebook:* main week notebook.

10. **Mini Data Exploration (Histogram)**
    Generate 200 random floats in `[0,1]`, compute mean/median/variance, and plot a histogram with `matplotlib`.
    **Dedicated notebook required:** `w01_ex10_exploration.ipynb`

---

## 📅 Week 2 — Functions, Errors & Functional Programming

Focus: **CP06–CP07 & CP10** (custom functions, exceptions, lambda/map/filter)

**Suggested main notebook:** `w02_functions_and_fp.ipynb`

1. **Reusable Stats Functions**
   Write functions `mean(xs)`, `stdev(xs)`, and `zscores(xs)` (returning a list). Add docstrings and simple doctests.
   *Notebook:* main week notebook.

2. **Robust Division (Exceptions)**
   Implement `safe_div(x, y)` that raises a `ValueError` with a clear message on invalid inputs; add `try/except` usage examples.
   *Notebook:* main week notebook.

3. **User Input, Else & Finally**
   Function that reads an integer from input, handles non‑numeric values, uses `else` for success and `finally` to print a closing message.
   *Notebook:* main week notebook.

4. **Lambda Warm‑up**
   Create `apply_twice(f, x)` and test with a few `lambda`s (e.g., `lambda x: 2*x`, `lambda s: s.strip().upper()`).
   *Notebook:* main week notebook.

5. **Map/Filter Mini‑Pipeline**
   Given a list of numbers, square them (`map`) and keep only those > 40 (`filter`). Show the before/after lists.
   *Notebook:* main week notebook.

6. **Functional Text Cleaning**
   Given a list of phrases, build a pipeline using lambdas + `map`/`filter` to: lowercase, strip, remove empty lines, and keep only phrases with ≥4 words.
   *Notebook:* main week notebook.

7. **Function Composition Utility**
   Write `compose(f, g)` returning a function `h(x)=f(g(x))`. Demonstrate with numeric and string examples.
   *Notebook:* main week notebook.

8. **From‑Scratch Linear Regression (No sklearn)**
   Generate synthetic `(x, y)` with noise; compute slope/intercept using means, covariance, and variance; plot points + fitted line.
   **Dedicated notebook required:** `w02_ex08_linear_regression_scratch.ipynb`

9. **Outlier‑Safe Mean (Exceptions + FP)**
   Implement `trimmed_mean(xs, proportion)` that trims tails and averages the middle. Validate inputs (exceptions), then use `map`/`filter` where appropriate.
   *Notebook:* main week notebook.

10. **Small Coding Kata (Functions + Errors)**
    Write `parse_config(text)` that reads `key=value` lines into a dict, ignoring blanks and `#` comments. Validate duplicates and malformed lines with custom exceptions.
    **Dedicated notebook suggested:** `w02_ex10_parse_config.ipynb`

---

## 📅 Week 3 — Decorators, Dates/Times & First ML Steps

Focus: **CP08–CP09 & revisit CP10** (decorators, datetime, lambda/map usage in pipelines)

**Suggested main notebook:** `w03_decorators_datetime_ml.ipynb`

1. **Datetime Basics**
   Format today’s date, parse date strings, compute deltas (days between two dates), and add/subtract timedeltas.
   *Notebook:* main week notebook.

2. **`timeit` Decorator**
   Create a `@timeit` decorator that measures execution time. Compare a naive vs a vectorized operation (e.g., Python loops vs NumPy).
   *Notebook:* main week notebook.

3. **Logging Decorator**
   Create `@log_calls` that records function name, args/kwargs, and return value. Allow a parameter `level="INFO"|"DEBUG"`.
   *Notebook:* main week notebook.

4. **Caching/Memoization Decorator**
   Implement `@memoize` (or use `functools.lru_cache`) and demonstrate speedup on an expensive recursive function (e.g., Fibonacci).
   *Notebook:* main week notebook.

5. **Datetime mini‑project**
   Given a list of ISO date strings, parse, sort, compute average interval, and plot a simple line of counts per day.
   *Notebook:* main week notebook.

6. **Vector Dot Product — Three Ways**
   Implement dot product with pure Python, with `math.fsum`, and with NumPy. Compare correctness and performance using your `@timeit`.
   *Notebook:* main week notebook.

7. **K‑Nearest Neighbors (from scratch)**
   Implement a simple KNN classifier for 2D points: Euclidean distance, choose k neighbors, majority vote. Visualize decision boundary for a small grid.
   **Dedicated notebook required:** `w03_ex07_knn_scratch.ipynb`

8. **Functional Pipeline for Text**
   Build a mini text‑cleaning pipeline using `lambda/map/filter`: lowercase, strip, remove punctuation, drop stopwords. Show before/after examples and simple word counts.
   *Notebook:* main week notebook.

9. **Intro ML with scikit‑learn (Regression)**
   Use `sklearn.datasets.make_regression` to generate data, split train/test, fit `LinearRegression`, visualize predictions vs truth, report R² and coefficients.
   **Dedicated notebook suggested:** `w03_ex09_sklearn_linear_regression.ipynb`

10. **Stretch Goal: Classification with scikit‑learn**
    Use `make_classification`, split train/test, fit `KNeighborsClassifier` or `LogisticRegression`, compute accuracy, confusion matrix, and plot decision regions.
    **Dedicated notebook suggested:** `w03_ex10_sklearn_classification.ipynb`

---

## Submission & Presentation Tips

* Keep notebooks tidy: headings, short explanations, and clear outputs.
* Name dedicated notebooks exactly as requested (e.g., `w02_ex08_linear_regression_scratch.ipynb`).
* If you get stuck, add a short note describing the issue and your attempted approaches.
* Bonus points: add simple unit tests (e.g., in a `tests/` folder) for reusable functions.

Good luck and have fun — you’ve got this! 🚀