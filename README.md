# 🚀 Bayesian Black-Box Optimisation — Capstone Project

![Status](https://img.shields.io/badge/Status-COMPLETE-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Type](https://img.shields.io/badge/Type-Capstone-green)
![Modules](https://img.shields.io/badge/Modules-12--24-purple)
![Week](https://img.shields.io/badge/All%2013%20Weeks-Done-brightgreen)

## 📋 Documentation

| Document | Description |
|----------|-------------|
| [DATASHEET.md](DATASHEET.md) | Dataset documentation — composition, collection process, preprocessing and intended uses |
| [MODEL_CARD.md](MODEL_CARD.md) | Model card — GP-BBO approach, strategy evolution, performance and limitations |

---

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
| Module 20 | Week 9 | ✅ Complete | Tight trust regions, F5 ridge momentum, F1 narrow-spike anchor | 3/8 improved (F1 ⭐, F5 ⭐, F7 ⭐) |
| Module 21 | Week 10 | ✅ Complete | Ultra-tight exploit for F7/F8, F5 ridge micro-refinement | 2/8 improved (F7 ⭐, F8 ⭐) |
| Module 22 | Week 11 | ✅ Complete | Per-function momentum/recovery, manual overrides vs GP drift | 2/8 improved (F7 ⭐, F8 ⭐) |
| Module 23 | Week 12 | ✅ Complete | W11 bests as anchors, F5 ridge return, F7/F8 momentum | 1/8 improved (F8 ⭐ 9.9799) |
| Module 24 | Week 13 | ✅ Complete | FINAL: score-weighted centroid (F4/F6/F7), F5 boundary push 0.990, F8 trend | 3/8 improved (F1 ⭐+246%, F5 ⭐+10.6%, F7 ⭐) |

---

## 🏆 All-Time Best Results — FINAL

| Function | Best Result | Best Week | Notes |
|----------|-------------|-----------|-------|
| F1 | **0.33641** ⭐ | **Week 13** | x1=0.635 found true peak — 246% above previous best! |
| F2 | 0.6478 | Week 6 | Very noisy — same coords gave 0.465 in W11 |
| F3 | -0.0107 | Week 1 | Stuck — best result still from W1 across all 13 weeks |
| F4 | -0.1284 | Week 4 | Non-stationary; W13 score-weighted centroid gave -5.585 |
| F5 | **4039.88** ⭐ | **Week 13** | Removed 0.98 boundary cap — +388 pts (+10.6%) |
| F6 | -0.2037 | Week 8 | x4=0.718, x5=0.020 confirmed critical — never beaten |
| F7 | **3.1050** ⭐ | **Week 13** | Score-weighted centroid clinched final new best |
| F8 | 9.9799 | Week 12 | Trend extrapolation W10→W11→W12 — W13 just below |

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
| F4 | -0.1284 | ✅ First real improvement for F4 — all-time best |
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
| F8 | **9.9275** | ✅ All-time best at the time |

**3/8 improved (F5, F6, F8)**

---

### Week 6 (Module 17) — Per-Function Beta Tuning
| F | Result | Note |
|---|--------|------|
| F1 | **0.0880** | ✅ All-time best at the time — big jump |
| F2 | **0.6478** | ✅ All-time best — still unbeaten |
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
| F5 | **3632.18** | ✅ All-time best at the time ⭐ |
| F6 | **-0.2037** | ✅ All-time best — still unbeaten |
| F7 | **2.7440** | ✅ All-time best at the time ⭐ |
| F8 | 9.887 | ❌ Slight drop |

**3/8 improved (F5, F6, F7 — all new bests)**

---

### Week 9 (Module 20) — Tight Exploit + Narrow Spike Recovery
| F | Result | Note |
|---|--------|------|
| F1 | **0.09715** | ✅ All-time best ⭐ — tight anchor to x2=0.654 paid off |
| F2 | 0.5975 | ❌ Tiny x1 shift (+0.001) caused big drop — very noisy |
| F3 | -0.0533 | ❌ x3=0.382 vs W1's 0.475 |
| F4 | -14.466 | ❌ Near-exact W4 coords still volatile |
| F5 | **3651.37** | ✅ All-time best ⭐ — ridge peak at x1=0.027 |
| F6 | -0.2846 | ❌ x4 pushed too high |
| F7 | **2.9422** | ✅ All-time best at the time — strong momentum |
| F8 | 9.9270 | ❌ Missed W5 best by 0.0005 |

**3/8 improved (F1 ⭐, F5 ⭐, F7 ⭐)**

---

### Week 10 (Module 21) — Ultra-Tight F7/F8 Exploit
| F | Result | Note |
|---|--------|------|
| F1 | 0.09596 | ❌ Small drop from W9 best |
| F2 | 0.62631 | ❌ Recovering, not yet at W6 best |
| F3 | -0.04305 | ❌ Still stuck |
| F4 | -13.086 | ❌ Still volatile |
| F5 | 3651.356 | ❌ Missed W9 best by 0.015 — x1=0.010 slightly worse than 0.027 |
| F6 | -0.31774 | ❌ Recovery failed again |
| F7 | **3.0391** | ✅ All-time best at the time ⭐ — 5th consecutive improvement |
| F8 | **9.9616** | ✅ All-time best at the time ⭐ — ultra-tight recovery worked |

**2/8 improved (F7 ⭐, F8 ⭐)**

---

### Week 11 (Module 22) — Manual Overrides vs GP Drift
| F | Result | Note |
|---|--------|------|
| F1 | 0.09114 | ❌ Below W9 best (0.09715) |
| F2 | 0.4656 | ❌ Big drop — very noisy function |
| F3 | -0.0514 | ❌ Still stuck since W1 |
| F4 | -15.239 | ❌ Still volatile |
| F5 | 3651.353 | ❌ x1=0.005 slightly worse — ridge peak confirmed at x1=0.027 |
| F6 | -0.2783 | ❌ Improving but below W8 best |
| F7 | **3.1034** | ✅ All-time best ⭐ — 6 consecutive improvements W6→W11 |
| F8 | **9.9750** | ✅ All-time best ⭐ — momentum continues |

**2/8 improved (F7 ⭐, F8 ⭐)**

---

### Week 12 (Module 23) — Results in
| F | Submission | Result | Note |
|---|------------|--------|------|
| F1 | 0.651500-0.670000 | -0.0029 ❌ | x2=0.670 crashed — spike confirmed narrow at x2=0.654 |
| F2 | 0.704856-0.942000 | 0.5126 ❌ | x2=0.942 too high |
| F3 | 0.020000-0.954000-0.475000 | -0.0523 ❌ | x2=0.954 too low |
| F4 | 0.337655-0.667407-0.837231-0.628203 | -16.474 ❌ | W4 region still failing |
| F5 | 0.027000-0.980000-0.963000-0.979000 | 3463.42 ❌ | x3=0.963 caused 188-pt drop |
| F6 | 0.417095-0.367584-0.502073-0.701098-0.022008 | -0.3998 ❌ | x4=0.701 too low |
| F7 | 0.242071-0.235871-0.349962-0.303448-0.305843-0.659759 | 3.0986 ❌ | x6=0.660 vs W11's 0.643 slightly worse |
| F8 | 0.131852-0.171318-0.123876-0.228240-0.795114-0.554833-0.264222-0.564700 | **9.9799** ✅ | NEW ALL-TIME BEST |

**1/8 improved (F8 ⭐)**

---

### Week 13 (Module 24) — FINAL — Results In ✅
| F | Submission | Result | Note |
|---|------------|--------|------|
| F1 | 0.635000-0.654000 | **0.33641** ✅ | NEW ALL-TIME BEST — +246% above W9! x1=0.635 found the true peak |
| F2 | 0.722000-0.921380 | 0.4831 ❌ | Stochastic — W6 best (0.6478) stands |
| F3 | 0.050000-0.969910-0.474761 | -0.0298 ❌ | W1 best (-0.011) still unbeaten after 13 weeks |
| F4 | 0.358693-0.496383-0.626773-0.483600 | -5.585 ↑ | Not all-time best but best since W7 — centroid strategy worked |
| F5 | 0.027000-0.990000-0.990000-0.990000 | **4039.88** ✅ | NEW ALL-TIME BEST — +388 pts from removing 0.98 cap |
| F6 | 0.415859-0.378425-0.521334-0.722648-0.022901 | -0.3111 ❌ | W8 best (-0.2037) stands |
| F7 | 0.232699-0.231503-0.351373-0.289969-0.290607-0.646623 | **3.1050** ✅ | NEW ALL-TIME BEST — score-weighted centroid |
| F8 | 0.159000-0.209000-0.127000-0.190000-0.775000-0.520000-0.299000-0.591000 | 9.9676 ❌ | W12 best (9.9799) stands — trend didn't continue |

**3/8 new all-time bests in the final week — CAPSTONE COMPLETE**

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
2. **Log-transform outputs** — stabilise GP fitting across extreme output ranges (e.g. F5 at 3651 vs F1 at 0.097)
3. **Build candidate grid** — 50,000 LHS points, constrained to trust region around confirmed best X
4. **Fit GP** — Matérn kernel (ν=2.5), `normalize_y=True`, 3 restarts
5. **Score candidates** — compute UCB and EI across all candidates
6. **Ensemble selection** — pick candidate with higher GP posterior mean between UCB and EI winners
7. **Duplicate check** — auto-perturb if selected point is within 0.015 of any prior submission
8. **Manual override** — when GP contradicts consistent empirical trend, trust the trend
9. **Output** — portal submission string in `x1-x2-...-xn` format (6 decimal places)

### Key Techniques
- Log transforms for functions with extreme output ranges
- Yeo-Johnson transform for volatile functions (F4)
- 50,000 LHS candidate points per function for broad coverage
- Trust regions anchored to confirmed all-time best X (not GP best)
- Boundary clipping to [0.02, 0.98] — corner points consistently perform poorly
- Duplicate check to prevent resubmitting previously queried points
- Outlier removal before GP fit (F4: W2/W3 values of −26.59 and −26.07 excluded permanently)
- Recent-only GP for non-stationary functions (F4: uses only post-W4 data)
- Per-function policies: MOMENTUM / RECOVERY / NEAR-EXACT / RIDGE / BOLD-EXPLORE

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

### 🆕 Week 5–6 Improvements

| Fix | Detail |
|-----|--------|
| **Anchor to all-time best** | Trust center set explicitly to confirmed best known X (not GP best) |
| **Per-function beta** | Each function independently tuned — higher beta for stuck functions, lower for momentum |
| **F5 tightest exploit** | r=0.05, beta=0.05 — maximum exploitation of ridge |

### 🆕 Week 7–8 Improvements

| Fix | Detail |
|-----|--------|
| **Beta reduced globally** | High beta (>1.0) dropped; range settled to 0.3–0.8 |
| **F5 ridge committed** | x1 monotonically decreasing, x2–x4 converging to ~0.979 |
| **F6/F7 recovery anchor** | Returned to confirmed historical bests — produced new all-time bests |

### 🆕 Week 9 Improvements

| Fix | Detail |
|-----|--------|
| **F1 x2 corrected** | W8 drifted x2 to 0.704 from optimal 0.652 — radius cut to 0.03 |
| **F5 ridge peak found** | x1=0.027 confirmed as ridge peak (3651.37) — best result in project |
| **Manual GP override** | GP suggested x2=0.966 for F5, contradicting trend — overridden manually |

### 🆕 Week 10–11 Improvements

| Fix | Detail |
|-----|--------|
| **F4 recent-only GP** | Landscape non-stationarity detected — GP rebuilt using only recent observations (W4+) |
| **F7 6-week streak** | Consecutive improvements W6→W11 by using tight trust regions around each week's new best |
| **F8 ultra-tight** | W10→W11 momentum confirmed; tiny steps in 8D space outperform large jumps |
| **F5 ridge reversal** | Going below x1=0.027 (0.010, 0.005) made it slightly worse — return to 0.027 in W12 |

---

### Final Per-Function Results Summary

| Function | All-time Best | Best Week | Final Strategy That Worked |
|----------|-------------|-----------|--------------------------|
| F1 | **0.33641** ⭐ | **W13** | x2=0.654 locked; x1=0.635 (not 0.6515!) found true peak |
| F2 | 0.6478 | W6 | Stochastic — best draw at (0.7049, 0.9214) was W6 |
| F3 | -0.0107 | W1 | x2=0.9699 + x3=0.4748 + x1≈0.02 — W1 result never beaten |
| F4 | -0.1284 | W4 | Non-stationary; W4 region unreproducible — W7 region safer |
| F5 | **4039.88** ⭐ | **W13** | Remove 0.98 cap on x2-x4; x1=0.027 ridge peak |
| F6 | -0.2037 | W8 | x4=0.718, x5=0.020 critical; W8 result never beaten |
| F7 | **3.1050** ⭐ | **W13** | Score-weighted centroid of W10/W11/W12 confirmed bests |
| F8 | 9.9799 | W12 | Trend extrapolation W10→W11→W12; 4 consecutive new bests |

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
| W9 | Verify GP suggestion direction against empirical trends — GP suggested decreasing x2 for F5; data said keep it at 0.979 |
| W10 | F4 shows non-stationarity: same W4 coords gave −0.128 in W4 and −14.5 in W9. Use recent-only GP for non-stationary landscapes |
| W11 | Manual overrides beat raw GP when empirical evidence is clear — F5 ridge peak at x1=0.027 outperformed GP's preference to push lower |
| W12 | Ridge width: x3 deviation of just 0.016 (from 0.9795 to 0.963) caused 188-point drop in F5. Both x3 and x4 must stay at 0.979-0.980 on the ridge. |
| W12 | x2 in F1 is an extremely narrow spike: x2=0.670 (Δ=+0.016 from optimal 0.654) crashed output from 0.097 to −0.003. Never deviate more than 0.001 in x2 for F1. |
| W13 | Boundary caps can cost more than expected: removing the [0.02, 0.98] clip on F5's x2-x4 gained +388 points (+10.6%) in a single query. Always test at-boundary when a ridge is trending toward the edge. |
| W13 | The true peak of F1 (0.33641) was never near 0.6515 — it was at x1=0.635. A 0.016 shift in x1 (not x2) tripled the all-time best. Even well-explored functions can have untested neighbourhoods. |
| W13 | Score-weighted centroids (softmax weighting over confirmed-best observations) are a simple, powerful way to handle non-stationarity: instead of trusting one best point, weight all good points and let the centroid naturally drift toward the most reliable region. |

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
├── module-20/          ← Week 9: F1, F5 all-time bests; F7 momentum
│   ├── notebooks/
│   │   └── Module_20_Week9_Capstone.ipynb
│   └── plots/
│
├── module-21/          ← Week 10: F7, F8 all-time bests
│   ├── notebooks/
│   │   └── Module_21_Week10_Capstone.ipynb
│   └── plots/
│
├── module-22/          ← Week 11: F7 (3.1034), F8 (9.9750) all-time bests
│   ├── notebooks/
│   │   └── Module_22_Week11_Capstone.ipynb
│   └── plots/
│
├── module-23/          ← Week 12: F8 (9.9799) all-time best
│   ├── notebooks/
│   │   └── Module_23_Week12_Capstone.ipynb
│   └── plots/
│
└── module-24/          ← Week 13 FINAL: F1 (0.33641), F5 (4039.88), F7 (3.1050) NEW BESTS
    ├── notebooks/
    │   └── Module_24_Week13_Capstone.ipynb
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

3. Open the final notebook:
```bash
jupyter notebook module-24/notebooks/Module_24_Week13_Capstone.ipynb
```

---

## 📬 Contact

**Divya Bhanusri** — Imperial College AI/ML Programme

🔗 [GitHub Profile](https://github.com/divyabhanusri24)
