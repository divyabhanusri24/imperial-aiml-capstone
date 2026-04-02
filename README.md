# 🚀 Bayesian Black-Box Optimisation — Capstone Project

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Type](https://img.shields.io/badge/Type-Capstone-green)
![Modules](https://img.shields.io/badge/Modules-12--24-purple)

## 📄 Overview

This project is the Capstone requirement for the **Imperial College AI/ML Programme**, running from Module 12 through to Module 24.

The challenge involves optimising **8 unknown black-box functions** of increasing dimensionality (2D to 8D) using a limited number of weekly queries. Each week, one new input point per function is submitted via the capstone portal, and the resulting output is used to refine the search strategy.

The goal is to find the input that **maximises the output** of each function through intelligent, iterative, data-driven decisions — reflecting how optimisation is approached in real-world ML research.

---

## ❓ Problem Statement

Eight synthetic black-box functions are provided, each simulating a real-world optimisation challenge such as radiation detection, drug discovery, or hyperparameter tuning. The internal equations are unknown — only inputs and outputs are observable.

Each function must be maximised using limited weekly queries, making smart search strategy essential.

---

## 🎯 Project Goals

1. **Explore** unknown function landscapes intelligently
2. **Exploit** promising regions as data grows each week
3. **Iterate** and refine strategy based on weekly results
4. **Reflect** on approach and document decision-making throughout

---

## 📊 Functions Overview

| Function | Dimensions | Description |
|----------|------------|-------------|
| F1 | 2D | Radiation Detection |
| F2 | 2D | Noisy ML Model |
| F3 | 3D | Drug Discovery |
| F4 | 4D | Warehouse Placement |
| F5 | 4D | Chemical Yield |
| F6 | 5D | Cake Recipe Optimisation |
| F7 | 6D | ML Hyperparameter Tuning |
| F8 | 8D | Complex 8D Optimisation |

---

## 🗓️ Weekly Progress

| Module | Week | Status | Strategy Used | Result |
|--------|------|--------|---------------|--------|
| Module 12 | Week 1 | ✅ Complete | GP + UCB (adaptive beta), Matérn/RBF kernels, grid + random search | 6/8 functions improved |
| Module 13 | Week 2 | ✅ Complete | GP + UCB with log transforms, adaptive beta per function | 1/8 functions improved |
| Module 14 | Week 3 | ⏳ In Progress | Refining strategy based on Week 2 analysis | TBD |
| Module 15 | Week 4 | 🔜 Coming Soon | TBD | TBD |

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
- Weekly iteration: analyse results → adjust strategy → submit new points

### Lessons from Week 2
- Only 1/8 functions improved — indicates need for strategy refinement
- Exploring alternative acquisition functions and kernel configurations for Week 3

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|-------------|
| **Language** | Python |
| **Libraries** | NumPy, Matplotlib, Scikit-Learn, SciPy |
| **Models** | Gaussian Process and other surrogate models |
| **Tools** | Jupyter Notebooks, Git, GitHub |

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

3. Open notebook:
```bash
jupyter notebook module-12/notebooks/Module_12_Bayesian_Optimisation.ipynb
```

---

## 📬 Contact

**Divya Bhanusri** — Imperial College AI/ML Programme  
🔗 [GitHub Profile](https://github.com/divyabhanusri24)
