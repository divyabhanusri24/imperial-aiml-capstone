# Model Card — GP-BBO Optimisation Approach

*Following the Model Cards framework (Mitchell et al., 2019)*

---

## 1. Overview

| Field | Details |
|-------|---------|
| **Name** | GP-BBO with Trust Regions and Ensemble Acquisition |
| **Type** | Bayesian Optimisation surrogate model |
| **Version** | Week 10 (final evolved form) |
| **Surrogate** | Gaussian Process — Matérn kernel ν=2.5, normalize_y=True, 3 restarts |
| **Acquisition** | UCB + EI ensemble (winner = candidate with higher GP posterior mean) |
| **Candidates** | 50,000 Latin Hypercube Sampling points per function per week |
| **Framework** | scikit-learn GaussianProcessRegressor + scipy |

---

## 2. Intended Use

**What tasks is this approach suitable for?**
- Sample-efficient black-box optimisation where function evaluations are expensive or limited
- Iterative search with one or very few evaluations per cycle
- Maximisation of continuous functions over bounded input domains [0, 1]^n
- Research and teaching contexts requiring documented, reproducible optimisation decisions

**What use cases should be avoided?**
- Functions with known closed-form gradients — gradient-based methods will be faster and more accurate
- Functions suspected to be non-stationary or time-varying (the GP assumes the landscape is fixed — F4 in this project may violate this)
- Very high-dimensional spaces (n > 10) without dimensionality reduction — the LHS candidate coverage becomes inadequate
- Settings where the trust region anchor is unreliable (e.g. the confirmed best was obtained from a noisy or stochastic evaluation)

---

## 3. Details — Strategy Across Ten Rounds

**Weeks 1–3: Exploration phase**
Initial queries used broad GP+UCB with high beta values and no trust regions. Week 3 added SVM region classification to filter candidates — this produced 0/8 improvements and was permanently discarded. Key lesson: the dataset was too small for an SVM to learn meaningful boundaries.

**Weeks 4–6: Trust regions introduced**
From Week 4, all searches were anchored within a radius r around the confirmed all-time best input for each function. The UCB+EI ensemble replaced single-acquisition scoring. Per-function beta values were introduced (range: 0.02 to 2.5) based on how much exploration vs exploitation each function needed. Outlier exclusion for F4 was introduced (Week 2: −26.59, Week 3: −26.07).

**Weeks 7–9: Per-function policies**
Each function was assigned a named policy — MOMENTUM (improving), RECOVERY (regressed), ANCHOR-TIGHT (stuck near a historic best), NEAR-EXACT (stochastic) — driving the trust radius and beta choice. Trust radii tightened from r=0.15–0.20 (early weeks) to r=0.02–0.08 (late weeks) as the strategy shifted from exploration to exploitation.

**Week 10: Peer-informed adjustments**
After reviewing classmates' strategies on the discussion board:
- **F4**: Switched to recent-only GP (initial data + Weeks 4, 7, 8, 9 only). Weeks 5 and 6 dropped as potentially reflecting a different landscape configuration. Trust radius widened to r=0.05 to compensate for the sparser training set.
- **F1**: GP suggested x2=0.674 but confirmed best has x2=0.654. Manually corrected to (0.651000, 0.654500) — peer insight that F1 may have a narrow spike the Matérn kernel averages away.
- **F5**: x1 manually set to 0.010, continuing a nine-week downward ridge (0.241 → 0.140 → 0.102 → 0.072 → 0.044 → 0.027 → 0.010). GP was over-ridden because the duplicate-check perturbation had previously reversed the trend.

---

## 4. Performance

**Best results achieved (all-time, as of Week 10 submission):**

| Function | Best Output | Best Week | Notes |
|----------|------------|-----------|-------|
| F1 | 0.09715 | Week 9 | Recovering after W7 near-zero result |
| F2 | 0.6478 | Week 6 | Near plateau; very sensitive to x1 |
| F3 | −0.0107 | Week 1 | Stuck; 9 rounds haven't beaten W1 |
| F4 | −0.1284 | Week 4 | Volatile; near-exact W4 coords gave −14.5 in W9 |
| F5 | 3651.37 | Week 9 | Strong ridge; best in peer cohort |
| F6 | −0.2037 | Week 8 | Recovering after W9 regression |
| F7 | 2.9422 | Week 9 | Four consecutive improvements W6→W9 |
| F8 | 9.9275 | Week 5 | W9 missed by 0.0005 |

**Metric:** Raw function output (higher = better). No normalisation applied to reported values.

**Improvement rate:** 3/8 functions improved in Weeks 8 and 9. Weeks 1–3 averaged 2.3/8. The shift to trust regions in Week 4 produced the highest single-week improvement (4/8).

---

## 5. Assumptions and Limitations

**Key assumptions:**
1. **Local smoothness:** The GP assumes nearby inputs produce similar outputs (Matérn ν=2.5 implies twice differentiability). If a function has sharp discontinuities or isolated spikes, the GP systematically underestimates the true maximum and misrepresents the basin width. F1 is the most likely violator.
2. **Stationarity:** The GP assumes the function landscape does not change between queries. F4 appears to violate this — the same coordinates returned −0.128 in Week 4 and −14.5 in Week 9.
3. **Trust region validity:** The approach assumes the confirmed best input is a reliable anchor. For stochastic or non-stationary functions, this anchor may not represent a stable optimum.

**Failure modes:**
- **Premature exploitation:** Tightening the trust radius too early can permanently trap the search in a local optimum. F3 demonstrates this — the Week 1 best has not been beaten in nine subsequent rounds.
- **Duplicate perturbation errors:** The auto-perturbation on duplicate detection can reverse a known trend (occurred with F5 in an earlier round). Manual overrides are required when the GP contradicts a clear data pattern.
- **Convergence warnings on F4:** The GP throws a lower-bound warning on the length scale parameter, indicating the surrogate cannot fit a coherent smooth surface. Predictions for F4 should be treated as weakly informative rather than reliable.

**Computational constraints:**
All GP fits run on a local CPU. With 50,000 LHS candidates and up to 20 training points, fit time is under 60 seconds per function. Scaling to higher observation counts or larger candidate pools would require GPU acceleration or sparse GP approximations.

---

## 6. Ethical Considerations

**Transparency and reproducibility:**
Every submission in this project is traceable. The GitHub repository contains the full query history, per-function policy decisions, and manual override rationale. A reviewer with access to the initial `.npy` data files, the notebook code, and the portal output values can reproduce every GP fit and acquisition function score. The manual overrides (F1, F5, F4 in Week 10) are documented with explicit reasoning in the notebook cells, not hidden in undocumented post-processing.

**Why this matters beyond the capstone:**
In real-world applications of Bayesian Optimisation — drug discovery, materials science, hyperparameter tuning — the query budget is often genuinely expensive (lab time, compute cost, patient risk). A documented, auditable decision trail of the kind maintained here supports:
- **Error detection:** If a result later appears anomalous, the log identifies exactly which observation caused the GP to shift direction
- **Handover:** Another researcher can continue the optimisation from Week 10 without re-running the full history
- **Bias awareness:** The dataset explicitly documents where the sampling distribution is concentrated and where coverage is absent, rather than presenting results as if the search were uniform

**Limitations of the current transparency record:**
The manual override process, while documented, relies on the researcher recognising when the GP should not be trusted — a judgement call that cannot be fully automated. Future iterations could formalise this with anomaly detection or out-of-distribution checks on the acquisition function scores before the submission is locked.
