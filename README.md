# 🚀 Bayesian Black-Box Optimisation — Capstone Project

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Type](https://img.shields.io/badge/Type-Capstone-green)
![Modules](https://img.shields.io/badge/Modules-12--24-purple)

## 📄 Overview

This project is the Capstone requirement for the **Imperial College AI/ML Programme**, running from Module 12 through to Module 24.

The challenge involves optimising **8 unknown black-box functions** of increasing dimensionality (2D to 8D) using a limited number of weekly queries. Each week, one new input point per function is submitted via the capstone portal, and the resulting output is used to refine the search strategy.

The goal is to find the input that **maximises** the output of each function through intelligent, iterative, data-driven decisions — reflecting how optimisation is approached in real-world ML research and industry applications such as hyperparameter tuning, drug discovery, and industrial process optimisation.

### 💼 Career Relevance

This project directly builds skills needed for data science and ML engineering roles — making decisions under uncertainty, working with limited and expensive-to-acquire data, and iterating strategies based on evidence. These competencies apply to model tuning, A/B testing, experimental design, and any scenario where complete knowledge of the system is unavailable.

---

## ❓ Problem Statement

Eight synthetic black-box functions are provided, each simulating a real-world optimisation challenge such as radiation detection, drug discovery, or hyperparameter tuning. The internal equations are unknown — only inputs and outputs are observable.

Each function must be **maximised** using limited weekly queries, making smart search strategy essential.

---

## 🎯 Project Goals

1. **Explore** unknown function landscapes intelligently
2. **Exploit** promising regions as data grows each week
3. **Iterate** and refine strategy based on weekly results
4. **Reflect** on approach and document decision-making throughout

---

## 📊 Functions Overview

| Function | Dimensions | Description | Application |
|----------|-----------|-------------|-------------|
| F1 | 2D | Radiation Detection | Identify contamination sources in a 2D field |
| F2 | 2D | Noisy ML Model | Maximise log-likelihood with noisy outputs |
| F3 | 3D | Drug Discovery | Minimise side effects (negated for maximisation) |
| F4 | 4D | Warehouse Placement | Optimise product placement across warehouses |
| F5 | 4D | Chemical Yield | Maximise yield of a chemical process (unimodal) |
| F6 | 5D | Cake Recipe Optimisation | Maximise recipe score (negative by design, push toward zero) |
| F7 | 6D | ML Hyperparameter Tuning | Maximise model accuracy/F1 score |
| F8 | 8D | Complex 8D Optimisation | Maximise validation accuracy across 8 hyperparameters |

---

## 📥 Inputs and Outputs

**Inputs:** Each query is a numerical vector with all values constrained to [0, 1], submitted as a hyphen-separated string with six decimal places.

Example (4D function): `0.241041-0.805036-0.948951-0.905090`

**Outputs:** A single scalar value. **Higher output = better** (all functions are maximisation tasks).

**Initial data:** 10 observations per function provided as `.npy` files, growing by one point per week.

---

## 🗓️ Weekly Progress

| Module | Week | Status | Strategy Used | Result |
|--------|------|--------|---------------|--------|
| Module 12 | Week 1 | ✅ Complete | GP + UCB (adaptive beta), Matérn/RBF kernels, grid + random search | 6/8 functions improved |
| Module 13 | Week 2 | ✅ Complete | GP + UCB with log transforms, adaptive beta per function | 1/8 functions improved |
| Module 14 | Week 3 | ✅ Complete | GP + UCB (corrected strategy) + SVM region classification | Awaiting results |
| Module 15 | Week 4 | 🔜 Coming Soon | TBD | TBD |

### 🔑 Key Insight After Week 2

After Week 2, I confirmed that the goal is **maximisation** (higher output = better). This reversed my interpretation of several results — what I thought was an improvement for F4 (going to -26.59) was actually a disaster, while F5's output of 1450 was my best result across all functions. This discovery led to a complete restructuring of my Week 3 strategy.

---

## 🔬 Strategy & Approach

### Core Method
- **Surrogate Model:** Gaussian Process (GP) Regression
- **Acquisition Function:** Upper Confidence Bound (UCB)
- **Kernels:** Matérn and RBF (selected per function)
- **Beta Tuning:** Adaptive per-function beta values to balance exploration vs exploitation

### Key Techniques
- Log transforms for functions with extreme output ranges
- Grid search for low-dimensional functions (2D–3D)
- Random search for higher-dimensional functions (4D–8D)
- Trust region checks to verify query points stay near best known regions
- Boundary avoidance (values near 0.0 or 1.0 tend to perform poorly)
- Weekly iteration: analyse results → adjust strategy → submit new points

### 🆕 Week 3 Addition: SVM Region Classification

In Week 3, I introduced **Support Vector Machines** as a supplementary analysis tool:

- **Soft-margin SVM with RBF kernel** classifies observed points as high-performing vs low-performing
- Uses median output as the classification threshold
- Feature means comparison reveals which input dimensions tend to produce higher outputs
- SVM serves as a **supporting tool for region identification**, complementing the GP surrogate
- With 12 data points per function, SVM classification is exploratory but becomes more reliable as data grows

### Per-Function Strategy (Week 3)

| Function | Best Result | Best Week | Beta | Strategy |
|----------|-----------|-----------|------|----------|
| F1 | 2.82e-04 | W2 | 3.5 | Explore — both weeks near zero |
| F2 | 0.171 | W2 | 2.5 | GP-UCB explore near W2 region |
| F3 | -0.011 | W1 | 2.0 | Fine-tune W1 point |
| F4 | -0.346 | W1 | 3.0 | Reverse correction — W2 disaster recovery |
| F5 | **1450.94** | **W1 ⭐** | 0.3 | Exploit heavily — STAR performer |
| F6 | -0.361 | W1 | 2.0 | Fine-tune W1 region |
| F7 | 1.406 | W1 | 2.5 | GP-UCB explore more |
| F8 | 9.892 | W1 | 2.0 | GP-UCB balanced |

### Exploration vs Exploitation Balance

The balance varies per function and evolves weekly:
- **Heavy exploitation** for strong performers (F5: beta=0.3)
- **Heavy exploration** for stagnating functions (F1: beta=3.5, F4: beta=3.0)
- **Balanced approach** for steady progress functions (F3, F6, F8: beta=2.0)

### 📝 Lessons Learned

- **Week 1:** Broad exploration works well initially — 6/8 improved
- **Week 2:** Aggressive model-driven queries can backfire (F4: -0.35 → -26.59)
- **Week 3:** Understanding the objective (maximise vs minimise) is fundamental — always verify assumptions before iterating

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|-------------|
| Language | Python |
| Libraries | NumPy, Matplotlib, Scikit-Learn, SciPy |
| Models | Gaussian Process, SVM (SVC with RBF kernel) |
| Tools | Jupyter Notebooks, Git, GitHub |

---

## 📁 Repository Structure
```
imperial-aiml-capstone/
│
├── README.md
│
├── module-12/
│   ├── notebooks/
│   │   └── Module_12_Bayesian_Optimisation.ipynb
│   └── plots/
│
├── module-13/
│   ├── notebooks/
│   │   └── Module_13_Week2_Capstone.ipynb
│   └── plots/
│
├── module-14/
│   ├── notebooks/
│   │   └── Module_14_Week3_Capstone.ipynb
│   └── plots/
│
└── ...
```

---

## 💻 How to Run

1. Clone the repository:
```bash
git clone https://github.com/divyabhanusri24/imperial-aiml-capstone.git
```

2. Install requirements:
```bash
pip install numpy matplotlib scikit-learn scipy
```

3. Open the latest notebook:
```bash
jupyter notebook module-14/notebooks/Module_14_Week3_Capstone.ipynb
```

---

## 📬 Contact

**Divya Bhanusri** — Imperial College AI/ML Programme

🔗 [GitHub Profile](https://github.com/divyabhanusri24)
