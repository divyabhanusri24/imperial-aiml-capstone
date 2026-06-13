# 🚀 Bayesian Black-Box Optimisation — Capstone Project

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Type](https://img.shields.io/badge/Type-Capstone-green)
![Modules](https://img.shields.io/badge/Modules-12--24-purple)
![Week](https://img.shields.io/badge/Current-Week%209-orange)

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
| Module 12 | Week 1 | ✅ Complete | GP + UCB (adaptive beta), Matérn/RBF kernels, grid + random search | 6/8 improved |
| Module 13 | Week 2 | ✅ Complete | GP + UCB with log transforms, adaptive beta per function | 1/8 improved (F1) |
| Module 14 | Week 3 | ✅ Complete | GP + UCB + SVM region classification | 0/8 improved — full regression |
| Module 15 | Week 4 | ✅ Complete | GP + UCB + EI ensemble, trust regions, 50k candidates, outlier removal | 4/8 improved (F4, F5, F7, F8) |
| Module 16 | Week 5 | ✅ Complete | Trust regions anchored to all-time best points, dual-strategy F6 | 3/8 improved (F5, F6, F8) |
| Module 17 | Week 6 | ✅ Complete | Per-function beta tuning, UCB+EI ensemble, varied trust radii | 3/8 improved (F1, F2, F5) |
| Module 18 | Week 7 | ✅ Complete | Lower beta, tighter radii, locked onto confirmed best points | 1/8 improved (F5) |
| Module 19 | Week 8 | ✅ Complete | Recovery anchors, tightest F5 exploit, F6/F7 recovery from bests | 3/8 improved (F5 ⭐, F6 ⭐, F7 ⭐) |
| Module 20 | Week 9 | 🔄 Submitted | Tighter trust regions, F5 momentum ridge, strict anchoring for stuck functions | Awaiting results |
| Module 21 | Week 10 | ⏳ Upcoming | — | — |
| Module 22 | Week 11 | ⏳ Upcoming | — | — |
| Module 23 | Week 12 | ⏳ Upcoming | — | — |
| Module 24 | Week 13 | ⏳ Final | — | — |

---

## 🏆 All-Time Best Results (after Week 8)

| Function | Best Result | Best Week | Notes |
|----------|-------------|-----------|-------|
| F1 | 0.0880 | Week 6 | Stable — recovering to this region in W9 |
| F2 | 0.6478 | Week 6 | Near plateau around x2 ≈ 0.921 |
| F3 | -0.0107 | Week 1 | Stuck — best result still from W1 |
| F4 | -0.1284 | Week 4 | Volatile — W2/W3 outliers excluded from GP |
| F5 | **3632.18** ⭐ | **Week 8** | Strong upward trend across W4–W8 |
| F6 | **-0.2037** ⭐ | **Week 8** | New best — x5 small is the key signal |
| F7 | **2.7440** ⭐ | **Week 8** | New best — recovery working after W7 drop |
| F8 | 9.9275 | Week 5 | Unchanged since W5 — targeting W5 region in W9 |

---

## 📈 Week-by-Week Results Detail

### Week 1 (Module 12) — Broad Exploration
| F | Result | Note |
|---|--------|------|
| F3 | -0.011 | ✅ Best — still the all-time best for F3 |
| F6 | -0.361 | ✅ Best at the time |
| Others | — | Broad GP+UCB scan across full domain |

**6/8 functions improved**

---

### Week 2 (Module 13) — UCB with Log Transforms
| F | Result | Note |
|---|--------|------|
| F1 | 2.82e-04 | ✅ Best at the time |
| F4 | -26.59 | ❌ Extreme outlier — excluded from all future GP fits |

**1/8 improved (F1)**

---

### Week 3 (Module 14) — SVM Region Filter (Failed)
| F | Result | Note |
|---|--------|------|
| F4 | -26.07 | ❌ Another extreme outlier |
| All others | — | ❌ SVM filter caused overexploration |

**0/8 improved. Lesson: never use SVM as region filter on < 15 points**

---

### Week 4 (Module 15) — Trust Regions + EI Ensemble
| F | Result | Note |
|---|--------|------|
| F4 | -0.1284 | ✅ First real improvement for F4 |
| F5 | 2496.35 | ✅ Massive jump ⭐ |
| F7 | 2.671 | ✅ Best at the time |
| F8 | 9.897 | ✅ Best at the time |

**4/8 improved (F4, F5, F7, F8)**

---

### Week 5 (Module 16) — Anchored Trust Regions
| F | Result | Note |
|---|--------|------|
| F1 | 8.11e-05 | ❌ |
| F2 | 0.5834 | ❌ |
| F3 | -0.0187 | ❌ |
| F4 | -13.98 | ❌ Regression |
| F5 | 2941.85 | ✅ Beat W4 |
| F6 | -0.2999 | ✅ Best at the time |
| F7 | 1.6608 | ❌ |
| F8 | **9.9275** | ✅ All-time best — still unbeaten |

**3/8 improved (F5, F6, F8)**

---

### Week 6 (Module 17) — Per-Function Beta Tuning
| F | Result | Note |
|---|--------|------|
| F1 | **0.0880** | ✅ All-time best — big jump from 2.82e-04 |
| F2 | **0.6478** | ✅ All-time best |
| F3 | -0.0868 | ❌ |
| F4 | -21.25 | ❌ Regression |
| F5 | 3303.92 | ✅ Continued improvement |
| F6 | -0.5181 | ❌ Regression |
| F7 | 2.1498 | ❌ |
| F8 | 9.8116 | ❌ |

**3/8 improved (F1, F2, F5)**

---

### Week 7 (Module 18) — Lower Beta, Tighter Radii
| F | Result | Note |
|---|--------|------|
| F1 | 3.88e-13 | ❌ Crashed — x2 drifted 0.05 away from W6 optimum |
| F2 | 0.6476 | ❌ Near plateau |
| F3 | -0.0384 | ❌ |
| F4 | -4.94 | ❌ Volatile |
| F5 | **3626.83** | ✅ Best at the time — upward trend confirmed |
| F6 | -0.3390 | ❌ Regression |
| F7 | 2.5916 | ❌ |
| F8 | 9.8171 | ❌ |

**1/8 improved (F5 only)**

---

### Week 8 (Module 19) — Recovery Anchors + F5/F6/F7 Exploit
| F | Result | Note |
|---|--------|------|
| F1 | -0.000114 | ❌ Still off from W6 best |
| F2 | 0.6409 | ❌ x2 pushed too high (0.924 vs optimal 0.921) |
| F3 | -0.1415 | ❌ Worst-ever result from full LHS exploration |
| F4 | -7.163 | ❌ Volatile |
| F5 | **3632.18** | ✅ All-time best ⭐ |
| F6 | **-0.2037** | ✅ All-time best ⭐ |
| F7 | **2.7440** | ✅ All-time best ⭐ |
| F8 | 9.887 | ❌ Slight drop |

**3/8 improved (F5, F6, F7 — all new bests)**

---

### Week 9 (Module 20) — Submitted, Awaiting Results
| F | Trust Center | Radius | Policy | Key Change from W8 |
|---|-------------|--------|--------|--------------------|
| F1 | W6 best (0.6534, 0.6529) | r=0.03 | RECOVERY | Tightened from r=0.06; x2 corrected back to ~0.653 |
| F2 | W6 best (0.7049, 0.9214) | r=0.03 | PLATEAU | x2 held near 0.921, not pushed to 0.930 |
| F3 | W1 best (0.0206, 0.9699, 0.4748) | r=0.12 | ANCHOR | W8 full LHS produced worst-ever — returned to W1 region |
| F4 | W4 best (0.3530, 0.6516, 0.8054, 0.6161) | r=0.06 | TIGHT RECOVERY | Radius tightened from 0.15 → 0.06 |
| F5 | W8 best (0.0441, 0.9799, 0.9782, 0.9787) | r=0.02 | MOMENTUM | x2-x4 preserved at 0.979-0.980 ridge |
| F6 | W8 best (0.4093, 0.3607, 0.5029, 0.7183, 0.0203) | r=0.06 | MOMENTUM | Exploit new best, x5 kept small |
| F7 | W8 best (0.1386, 0.3299, 0.3256, 0.2643, 0.2953, 0.6511) | r=0.10 | MOMENTUM | Exploit new best, upward trend |
| F8 | W5 best (0.0898, 0.0683, 0.1810, 0.3273, 0.7662, 0.6534, 0.1748, 0.4992) | r=0.12 | RECOVERY | Tightened from r=0.20 to stay closer to W5 peak |

---

## 🔬 Strategy & Approach

### Core Method
- **Surrogate Model:** Gaussian Process (GP) Regression with Matérn kernel (ν=2.5)
- **Acquisition Functions:** Upper Confidence Bound (UCB) + Expected Improvement (EI) — ensemble
- **Beta Tuning:** Adaptive per-function beta values to balance exploration vs exploitation
- **Trust Regions:** Constrain search to neighbourhood of confirmed best known point (Week 4+)
- **Candidate Sampling:** 50,000 Latin Hypercube points per function

### 🔄 How the Pipeline Works

Each weekly notebook runs all 8 functions through a single parameterised function, keeping the entire strategy in one file. The core loop per function:

1. **Load data** — stack initial `.npy` observations with all weekly submissions and results
2. **Log-transform outputs** — stabilise GP fitting across extreme output ranges (e.g. F5 at 3632 vs F1 at 0.088)
3. **Build candidate grid** — 50,000 LHS points, constrained to trust region around confirmed best X
4. **Fit GP** — Matérn kernel (ν=2.5), `normalize_y=True`, 3 restarts
5. **Score candidates** — compute UCB and EI across all candidates
6. **Ensemble selection** — pick candidate with higher GP posterior mean between UCB and EI winners
7. **Duplicate check** — auto-perturb if selected point is within 0.015 of any prior submission
8. **Output** — portal submission string in `x1-x2-...-xn` format (6 decimal places)

### Key Techniques
- Log transforms for functions with extreme output ranges
- Yeo-Johnson transform for volatile functions (F4)
- 50,000 LHS candidate points per function for broad coverage
- Trust regions anchored to confirmed all-time best X (not GP best)
- Boundary clipping to [0.02, 0.98] — corner points consistently perform poorly
- Duplicate check to prevent resubmitting previously queried points
- Outlier removal before GP fit (F4: W2/W3 values of −26.59 and −26.07 excluded permanently)
- Per-function policies: MOMENTUM / RECOVERY / ANCHOR / PLATEAU / STUCK-EXPLORE

---

### 🆕 Week 4 Improvements

| Fix | Detail |
|-----|--------|
| **UCB + EI Ensemble** | Both acquisition functions computed; candidate with higher GP posterior mean selected |
| **Trust regions** | Search constrained to radius r around best known X — prevents W3-style overexploration |
| **50,000 candidates** | Up from 5–10k; better coverage especially for high-dimensional functions |
| **Boundary clip 0.02–0.98** | Removed corner-point bias present in W1–W3 |
| **F4 outlier removal** | W2 (−26.59) and W3 (−26.07) stripped before GP fit permanently |
| **Duplicate check** | Auto-perturbs query if too close (< 0.015) to any prior submission |

### 🆕 Week 5 Improvements

| Fix | Detail |
|-----|--------|
| **Anchor to all-time best** | Trust center set explicitly to confirmed best known X (not GP best) |
| **F5 tightest exploit** | r=0.05, beta=0.05 — maximum exploitation of 2496 peak |
| **F6 dual strategy** | Wide LHS vs W1 trust region — GP mean selected W1 trust region |
| **Full history tracked** | All weekly submissions included in duplicate check |

### 🆕 Week 6 Improvements

| Fix | Detail |
|-----|--------|
| **Per-function beta** | Each function independently tuned — higher beta for stuck functions, lower for momentum |
| **F1/F2 wider search** | Slightly broader trust regions discovered new all-time bests (0.0880 and 0.6478) |
| **F5 x1 trend identified** | Observed x1 decreasing pattern across W4→W5→W6 submissions |

### 🆕 Week 7 Improvements

| Fix | Detail |
|-----|--------|
| **Beta reduced** | High beta (>1.0) dropped; range settled to 0.3–0.8 across functions |
| **Radii tightened** | Regressions in W5–W6 linked to drifting too far from confirmed bests |
| **F5 ridge confirmed** | x1 monotonically decreasing, x2–x4 converging to ~0.979 — committed to this pattern |

### 🆕 Week 8 Improvements

| Fix | Detail |
|-----|--------|
| **F5 ultra-tight** | r=0.03 around W7 best — produced all-time best 3632.18 |
| **F6 recovery anchor** | Returned to W5 best region — produced all-time best −0.2037 |
| **F7 recovery anchor** | Returned to W4 best region — produced all-time best 2.7440 |
| **Lesson: F3 full LHS failed** | Broad exploration produced worst-ever F3 result (−0.1415) |

### 🆕 Week 9 Improvements

| Fix | Detail |
|-----|--------|
| **F1 x2 corrected** | W8 drifted x2 to 0.704 from optimal 0.652 — radius cut to 0.03 |
| **F2 x2 held firm** | Data shows x2 > 0.921 consistently hurts; trust region prevents GP pushing beyond 0.924 |
| **F3 re-anchored to W1** | Returned to W1 best after W8 full LHS disaster |
| **F4 radius tightened** | 0.15 → 0.06 around W4 best; Yeo-Johnson transform retained |
| **F5 x2-x4 preserved** | GP suggestion had x2 dropping to 0.966 — overridden to keep x2-x4 at ~0.979 |
| **F8 radius tightened** | 0.20 → 0.12 to stay in W5 neighbourhood |

---

### Per-Function Strategy Summary (Week 9 — current)

| Function | All-time Best | Beta | Trust Radius | Trust Center | Policy |
|----------|-------------|------|-------------|-------------|--------|
| F1 | 0.0880 (W6) | 0.5 | 0.03 | W6 best | RECOVERY |
| F2 | 0.6478 (W6) | 0.2 | 0.03 | W6 best | PLATEAU |
| F3 | -0.0107 (W1) | 1.5 | 0.12 | W1 best | ANCHOR |
| F4 | -0.1284 (W4) | 0.8 | 0.06 | W4 best | TIGHT RECOVERY |
| F5 | **3632.18 (W8)** ⭐ | 0.02 | 0.02 | W8 best | MOMENTUM |
| F6 | **-0.2037 (W8)** ⭐ | 0.3 | 0.06 | W8 best | MOMENTUM |
| F7 | **2.7440 (W8)** ⭐ | 0.5 | 0.10 | W8 best | MOMENTUM |
| F8 | 9.9275 (W5) | 0.8 | 0.12 | W5 best | RECOVERY |

---

### 📝 Lessons Learned

| Week | Lesson |
|------|--------|
| W1 | Broad exploration works well early — 6/8 improved from initial GP+UCB scan |
| W2 | Aggressive UCB on noisy functions causes extreme outliers (F4: −26.59) — always exclude before fitting |
| W3 | High beta + SVM region filter on < 15 points = overexploration disaster. Never use SVM as region filter |
| W4 | Trust regions are essential after regression; EI is more conservative than UCB alone |
| W5 | Anchor trust center to all-time best X, not GP best. Dual-strategy comparison useful for stuck functions |
| W6 | Per-function beta tuning outperforms a single global beta — each function needs different explore/exploit balance |
| W7 | Drifting even 0.05 in x2 for F1 crashed output from 0.088 → 3.88e-13. Stick to confirmed best coordinates |
| W8 | Full LHS for stuck functions produced worst-ever F3 result. Better to anchor to historical best than explore blindly |
| W9 | Verify GP suggestion direction against empirical trends before accepting — GP suggested x2=0.966 for F5, contradicting clear evidence |

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|-------------|
| Language | Python |
| Libraries | NumPy, Matplotlib, Scikit-Learn, SciPy |
| Models | Gaussian Process (Matérn ν=2.5) |
| Sampling | Latin Hypercube Sampling (scipy.stats.qmc) |
| Transforms | Log, Yeo-Johnson (for volatile functions like F4) |
| Tools | Jupyter Notebooks, Git, GitHub |

---

## 📁 Repository Structure

```
imperial-aiml-capstone/
│
├── README.md
├── REFERENCES.md
│
├── data/
│   ├── function_1/   (initial_inputs.npy, initial_outputs.npy)
│   ├── function_2/
│   └── ... (function_3 through function_8)
│
├── module-12/          ← Week 1: Broad GP+UCB exploration
│   ├── notebooks/
│   │   └── Module_12_Bayesian_Optimisation_Capstone.ipynb
│   └── plots/
│
├── module-13/          ← Week 2: UCB with log transforms
│   ├── notebooks/
│   │   └── Module_13_Week2_Capstone.ipynb
│   └── plots/
│
├── module-14/          ← Week 3: SVM filter (failed)
│   ├── notebooks/
│   │   └── Module_14_Week3_Capstone.ipynb
│   └── plots/
│
├── module-15/          ← Week 4: Trust regions + EI ensemble
│   ├── notebooks/
│   │   └── Module_15_Week4_Capstone.ipynb
│   └── plots/
│
├── module-16/          ← Week 5: Anchored trust regions
│   ├── notebooks/
│   │   └── Module_16_Week5_Capstone.ipynb
│   └── plots/
│
├── module-17/          ← Week 6: Per-function beta tuning (F1, F2, F5 new bests)
│   ├── notebooks/
│   │   └── Module_17_Week6_Capstone.ipynb
│   └── plots/
│
├── module-18/          ← Week 7: Tighter radii, lower beta
│   ├── notebooks/
│   │   └── Module_18_Week7_Capstone.ipynb
│   └── plots/
│
├── module-19/          ← Week 8: F5, F6, F7 all-time bests
│   ├── notebooks/
│   │   └── Module_19_Week8_Capstone.ipynb
│   └── plots/
│
└── module-20/          ← Week 9: Momentum + tighter recovery (submitted)
    ├── notebooks/
    │   └── Module_20_Week9_Capstone.ipynb
    └── plots/
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
jupyter notebook module-20/notebooks/Module_20_Week9_Capstone.ipynb
```

---

## 📬 Contact

**Divya Bhanusri** — Imperial College AI/ML Programme

🔗 [GitHub Profile](https://github.com/divyabhanusri24)
