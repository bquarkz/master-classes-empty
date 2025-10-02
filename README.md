# 🧪 Development Environment Setup — Master's Project (Python 3.12 + Conda + Jupyter)

This repository provides clear instructions to set up a clean and reproducible development environment using **Conda**, **Python 3.12**, and **JupyterLab**.
The structure is ideal for academic or research projects that use multiple notebooks and a reusable local Python library.
The environment is also ready to run tests with **pytest**.

The structure allows us to have a clean separation between the frontend (JupyterLab) and the backend (Python library).
Where Conda manages heavy dependencies (precompiled, like PyTorch, TensorFlow, scikit-learn, etc.), pip manages internal libraries (backend)
and can manage pure-Python packages as well. Unless you really know what you are doing, my recommendation is to use Conda for all packages
other than your backend. Doing that, you avoid dependency conflicts and keep your environment clean. Use pip only for your local library
(or for pure-Python packages when you understand the risks).

---

## 🧰 Prerequisites
py
Before starting, make sure you have:

* Anaconda 3
* macOS / Linux / Windows with a functional terminal
* Git

Verify Conda installation:

```bash
conda --version
```

---

## 🏗️ 1. Create the Conda environment

Create a new environment named `master-classes` with **Python 3.12**:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate master-classes
```

Remember to activate the environment every time you open a new terminal.
Your operating system has a Python installation by default; if you start changing packages and versions globally, you could cause problems.
That is why we use a local virtual environment (Conda).

As an exercise, after running the commands above, you can check the Python version:
```bash
python --version
```
It should be 3.12.x. And by using:
```bash
which python
```
you should see the path to the Python executable inside the Conda env, for example:
```aiignore
/opt/homebrew/anaconda3/envs/master-classes/bin/python
```

After activation your shell prompt should look like:
```bash
(master-classes) user@bla %
```

Important points:
1. Use a Conda environment created from `environment.yml`.
2. Install your backend code (see item 4) using pip while the Conda env is active.
3. Register the Jupyter kernel from that Conda env (see item 3) so notebooks use the same environment.
4. Let Conda manage dependencies; use pip only for your local backend (prefer `--no-deps`).
5. Work always with the Conda env activated when developing or running notebooks.
6. In notebooks, select the kernel created from the Conda env so it sees your egg-link and the Conda site-packages.
7. Egg-links will reflect code changes without reinstallation (use `%autoreload` in notebooks if helpful).

---

## 📦 2. Install essential packages

With the environment active, install the base data science and development packages:
```bash
conda env update -f environment.yml 
```

or install manually using:
```bash
conda install -c conda-forge numpy pandas matplotlib jupyterlab ipykernel
conda install -c conda-forge pytest black ruff mypy
```
The `-c conda-forge` flag is optional, we already set up the channel in the `environment.yml` file to always use the `conda-forge` channel.

> 💡 We recommend using the `conda-forge` channel, especially on macOS (Apple Silicon), because it provides more up-to-date and optimized binary builds.

---

## 📓 3. Register the environment as a Jupyter kernel (frontend)

To make the environment appear in Jupyter Notebook/Lab:
```bash
python -m ipykernel install --user --name master-classes --display-name "Master Classes (Python 3.12)"
```

After this, you'll see the kernel:
```
Python 3.12 (master-classes)
```
Inside JupyterLab's kernel selector. Be aware to be using that kernel to be able to access your backend code.

---

## 🧱 4. Install the local project library (backend)

If your project has a `pyproject.toml` and source code in `src/` (e.g., `src/unilab/`), install it in **editable mode**:

```bash
python -m pip install --no-deps --editable .
```

Notes:
- Use `--no-deps` to avoid pip trying to install or change dependencies that you manage with Conda.
- The `--editable` (`-e`) mode installs an egg-link pointing to your local source directory, so edits are immediately visible in notebooks.

---

## ➕ 5. Adding new packages

👉 If the package is **heavy or has binary dependencies** (e.g., scikit-learn, PyTorch, TensorFlow):

```bash
conda install -c conda-forge scikit-learn
```

👉 If it's a **pure Python library** from PyPI (use with care):

```bash
python -m pip install package-name
```

After installing new packages, you can update your environment file for reproducibility:

```bash
conda env export --from-history > after_environment.yml
```

---

## 🧪 6. Run tests

This project uses **pytest** for testing. Run tests with:

```bash
python -m pytest -q
```

---

## 🧭 7. Project structure

```text
.
├─ src/unilab/               # Local Python library (editable with pip install -e .)
├─ notebooks/                # Jupyter notebooks
├─ data/                     # Raw and processed data
├─ tests/                    # Unit tests
├─ reports/                  # Outputs, figures, reports
├─ scripts/                  # CLI and utility scripts
├─ environment.yml           # Conda environment definition
├─ pyproject.toml            # Project metadata and tool config
└─ README.md
```

---

## 🧼 8. Best practices

* ✅ Use **conda** for heavy or binary-dependent packages.
* ✅ Use **pip** only for your local library or pure Python packages.
* ✅ Avoid `pip install -U` for packages managed by conda.
* ✅ Version the `environment.yml` file, not the environment folder.
* ✅ If something breaks, it's usually faster to recreate the environment:

  ```bash
  conda env remove -n master-classes
  conda env create -f environment.yml
  ```

---

## ✨ Quick example

On your notebook:
```python
%load_ext autoreload
%autoreload 2

from unilab import hello, mean

hello("Your name here")
mean([10, 20, 30])
```

---

Happy coding 🧠🚀