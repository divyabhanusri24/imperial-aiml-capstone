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
| Module 14 | Week 3 | ✅ Complete | GP + UCB + SVM region classification | 0/8 improved — full regression |
| Module 15 | Week 4 | ✅ Complete | GP + UCB + EI ensemble, trust regions, 50k candidates, outlier removal | 4/8 improved (F4, F5, F7, F8) |
| Module 16 | Week 5 | ✅ Complete | Trust regions anchored to all-time best points, dual-strategy F6, tightest exploit on F5 | Submitted |

### 🏆 All-Time Best Results (after Week 5)

| Function | Best Result | Best Week |
|----------|-------------|-----------|
| F1 | 2.82e-04 | Week 2 |
| F2 | 0.611 | Initial data |
| F3 | -0.011 | Week 1 |
| F4 | -0.128 | Week 4 |
| F5 | **2496.35** | Week 4 |
| F6 | -0.361 | Week 1 |
| F7 | **2.671** | Week 4 |
| F8 | 9.897 | Week 4 |

---

## 🔬 Strategy & Approach

### Core Method
- **Surrogate Model:** Gaussian Process (GP) Regression with Matérn kernel (ν=2.5)
- **Acquisition Functions:** Upper Confidence Bound (UCB) + Expected Improvement (EI) — ensemble
- **Beta Tuning:** Adaptive per-function beta values to balance exploration vs exploitation
- **Trust Regions:** Constrain search to neighbourhood of best known point (Week 4+)

### 🔄 How the Pipeline Works

Each weekly notebook runs all 8 functions through a single parameterised function (`analyse_function_w5`), keeping the entire strategy in one file rather than separate notebooks per function. The core loop per function:

1. **Load data** — stack initial `.npy` observations with all weekly submissions and results
2. **Log-transform outputs** — stabilise GP fitting across extreme output ranges (e.g. F5 at 2496 vs F1 at 2.82e-04)
3. **Build candidate grid** — 50,000 LHS points, optionally constrained to a trust region around the best known X
4. **Fit GP** — Matérn kernel (ν=2.5), `normalize_y=True`, 3 restarts
5. **Score candidates** — compute UCB and EI across all candidates
6. **Ensemble selection** — pick the candidate with the higher GP posterior mean between UCB and EI winners
7. **Duplicate check** — auto-perturb if the selected point is within 0.015 of any prior submission
8. **Output** — portal submission string in `x1-x2-...-xn` format

### Key Techniques
- Log transforms for functions with extreme output ranges
- Grid search for low-dimensional functions (2D), LHS for higher-dimensional (3D–8D)
- 50,000 candidate points per function (Week 4+) for better search coverage
- Trust regions to prevent over-exploration after regressions
- Boundary clipping to [0.02, 0.98] — corner points consistently perform poorly
- Duplicate check to prevent resubmitting previously queried points
- Outlier removal before GP fit for disaster-affected functions (F4)
- Weekly iteration: analyse results → adjust strategy → submit new points

---

### 🆕 Week 4 Improvements

| Fix | Detail |
|-----|--------|
| **UCB + EI Ensemble** | Both acquisition functions computed; candidate with higher GP posterior mean selected |
| **Trust regions** | Search constrained to radius r around best known X — prevents W3-style overexploration |
| **50,000 candidates** | Up from 5–10k; better coverage especially for high-dimensional functions |
| **Boundary clip 0.02–0.98** | Removed corner-point bias present in W1–W3 |
| **F4 outlier removal** | W2 (−26.59) and W3 (−26.07) stripped before GP fit to avoid corrupting the model |
| **F5 manual fine-tune** | 50,000 micro-perturbations (±0.04) around W1 best [0.241, 0.805, 0.949, 0.905] |
| **Duplicate check** | Auto-perturbs query if too close (< 0.015) to any prior submission |

### 🆕 Week 5 Improvements

| Fix | Detail |
|-----|--------|
| **Anchor to all-time best** | Trust center set explicitly to best known X (not just GP best) |
| **F1 locked to W2 point** | Stop exploring — tight r=0.10 around [0.591, 0.591] that gave 2.82e-04 |
| **F2 anchored to initial** | Return to initial data point [0.703, 0.927] that gave 0.611 |
| **F5 tightest ever** | r=0.05, beta=0.05 — maximum exploitation of 2496 peak |
| **F6 dual strategy** | Wide LHS vs W1 trust region — GP mean selected W1 trust region |
| **F7/F8 tightened** | Radii reduced after W4 improvements confirmed |
| **W4 added to history** | All 4 weekly submissions now tracked for duplicate check |

### Per-Function Strategy Summary (Week 5)

| Function | All-time Best | Beta | Trust Radius | Mode |
|----------|-------------|------|-------------|------|
| F1 | 2.82e-04 (W2) | 1.0 | 0.10 on W2 point | Lock onto W2 — stop exploring |
| F2 | 0.611 (initial) | 0.5 | 0.15 on initial best | Return to origin of 0.611 |
| F3 | -0.011 (W1) | 1.0 | 0.12 on W1 | Tighter than W4 |
| F4 | -0.128 (W4) | 1.5 | 0.20 on W4 | Exploit first improvement |
| F5 | **2496.35 (W4) ⭐** | 0.05 | 0.05 on W4 | Maximum exploitation |
| F6 | -0.361 (W1) | 1.5 | 0.18 on W1 | W1 trust won dual-strategy test |
| F7 | 2.671 (W4) | 1.2 | 0.18 on W4 | Tighten after W4 success |
| F8 | 9.897 (W4) | 1.5 | 0.30 on W4 | Slightly wider for 8D gains |

### 📝 Lessons Learned

- **Week 1:** Broad exploration works well initially — 6/8 improved
- **Week 2:** Aggressive model-driven queries can backfire (F4: −0.35 → −26.59)
- **Week 3:** High beta + unreliable SVM on 12 pts = overexploration disaster — 0/8 improved
- **Week 4:** Trust regions are essential after regression; EI more disciplined than UCB alone; always check for duplicate submissions
- **Week 5:** Anchor trust center explicitly to all-time best X, not just GP best; dual-strategy comparison useful for stuck functions; tighter radius = more gain once you know the good region

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|-------------|
| Language | Python |
| Libraries | NumPy, Matplotlib, Scikit-Learn, SciPy |
| Models | Gaussian Process (Matérn), SVM (SVC with RBF kernel) |
| Sampling | Latin Hypercube Sampling (scipy.stats.qmc) |
| Tools | Jupyter Notebooks, Git, GitHub |

---

## 📁 Repository Structure

```
imperial-aiml-capstone/
│
├── README.md
│
├── data/
│   ├── function_1/   (initial_inputs.npy, initial_outputs.npy)
│   ├── function_2/
│   └── ... (function_3 through function_8)
│
├── module-12/
│   ├── notebooks/
│   │   └── Module_12_Bayesian_Optimisation_Capstone.ipynb
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
├── module-15/
│   ├── notebooks/
│   │   └── Module_15_Week4_Capstone.ipynb
│   └── plots/
│       └── w3_regression_analysis.png
│
├── module-16/
│   ├── notebooks/
│   │   └── Module_16_Week5_Capstone.ipynb
│   └── plots/
│       └── w4_progress_analysis.png
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
jupyter notebook module-16/notebooks/Module_16_Week5_Capstone.ipynb
```

---

## 📬 Contact

**Divya Bhanusri** — Imperial College AI/ML Programme

🔗 [GitHub Profile](https://github.com/divyabhanusri24)
