# CLAUDE.md — Imperial AIML Capstone Context

> Auto-loaded by Claude each session. Keep this updated after every weekly submission.

## Project Summary
- **Programme:** Imperial College AI/ML
- **Challenge:** Maximise 8 black-box functions using 1 query/week per function
- **Modules:** 12–24 | **Current Module:** 20 (Week 9 — notebook created, ready to run & submit)
- **Remaining:** Modules 20–24 (5 weeks left)

## 8 Functions at a Glance
| F | Dims | Domain | Goal |
|---|------|--------|------|
| F1 | 2D | Radiation detection | Max output |
| F2 | 2D | Noisy ML model | Max log-likelihood |
| F3 | 3D | Drug discovery | Max (minimise side effects, negated) |
| F4 | 4D | Warehouse placement | Max |
| F5 | 4D | Chemical yield (unimodal) | Max |
| F6 | 5D | Cake recipe | Max (negative scale, push to 0) |
| F7 | 6D | ML hyperparameter tuning | Max |
| F8 | 8D | Complex 8D optimisation | Max |

All inputs in [0, 1]^n. Submit as `x1-x2-...-xn` (6 decimal places).

---

## All-Time Best Results (update weekly)
| F | Best Output | Best X (submission string) | Week |
|---|------------|---------------------------|------|
| F1 | 0.0880 | 0.653384-0.652924 | W6 |
| F2 | 0.6478 | 0.704856-0.921380 | W6 |
| F3 | -0.0107 | 0.020584-0.969910-... (W1 notebook) | W1 |
| F4 | -0.1284 | 0.352971-0.651614-0.805417-0.616108 | W4 |
| F5 | **3632.18** | 0.044074-0.979912-0.978237-0.978721 | **W8** |
| F6 | **-0.2037** | 0.409346-0.360704-0.502905-0.718263-0.020264 | **W8** |
| F7 | **2.7440** | 0.138618-0.329866-0.325614-0.264255-0.295279-0.651123 | **W8** |
| F8 | 9.9275 | 0.089787-0.068251-0.180968-0.327284-0.766207-0.653365-0.174832-0.499246 | W5 |

## Week 8 Submissions (results pending)
| F | Submitted X | Strategy |
|---|------------|---------|
| F1 | 0.643797-0.704343 | MOMENTUM — trust W6 best, r=0.06, EI |
| F2 | 0.703797-0.924514 | MOMENTUM — trust W6 best, r=0.06, UCB+perturb |
| F3 | 0.100454-0.240875-0.185908 | STUCK-EXPLORE — full LHS, beta=2.5, EI |
| F4 | 0.383806-0.511512-0.656499-0.491038 | STUCK — trust W4 best, r=0.15, Yeo-Johnson |
| F5 | 0.044074-0.979912-0.978237-0.978721 | MOMENTUM — trust W7 best, r=0.03 (very tight) |
| F6 | 0.409346-0.360704-0.502905-0.718263-0.020264 | RECOVERY — trust W5 best, r=0.08 |
| F7 | 0.138618-0.329866-0.325614-0.264255-0.295279-0.651123 | RECOVERY — trust W4 best, r=0.15 |
| F8 | 0.182189-0.037358-0.268170-0.170921-0.585250-0.468337-0.247759-0.632930 | RECOVERY — trust W5 best, r=0.20 |

---

## Current Strategy (Week 8 / Module 19)
- **Surrogate:** GaussianProcessRegressor, Matérn ν=2.5, normalize_y=True, 3 restarts
- **Acquisition:** UCB + EI ensemble — pick candidate with higher GP posterior mean
- **Candidates:** 50,000 LHS points (scipy.stats.qmc.LatinHypercube)
- **Boundary clip:** [0.02, 0.98] — corners consistently perform poorly
- **Duplicate check:** perturb if new point < 0.015 from any prior submission
- **Trust regions:** constrain search to radius r around all-time best X

### Per-Function Settings (Week 8 — update for Week 9 when results arrive)
| F | Beta | Trust r | Trust Center | Policy | Notes |
|---|------|---------|-------------|--------|-------|
| F1 | 0.5 | 0.06 | W6 best | MOMENTUM | Improving — tight exploit |
| F2 | 0.3 | 0.06 | W6 best | MOMENTUM | Near plateau, micro-exploit |
| F3 | 2.5 | None | — | STUCK-EXPLORE | No improvement since W1, full LHS |
| F4 | 1.2 | 0.15 | W4 best | STUCK | Yeo-Johnson transform, alpha=0.1 |
| F5 | 0.05 | 0.03 | W7 best | MOMENTUM | Upward trend — tightest exploit |
| F6 | 0.3 | 0.08 | W5 best | RECOVERY | W7 regression — returning to W5 |
| F7 | 0.5 | 0.15 | W4 best | RECOVERY | W7 drop — returning to W4 best |
| F8 | 0.8 | 0.20 | W5 best | RECOVERY | Wider for 8D space |

---

## Data Pipeline (per function, each week)
1. Load `data/function_N/initial_inputs.npy` + `initial_outputs.npy`
2. Stack with all weekly submissions + results (hard-coded in notebook)
3. Log-transform outputs if range is extreme (F5 especially)
4. Generate 50k LHS candidates (clipped to [0.02, 0.98])
5. Optionally restrict candidates to trust region around best X
6. Fit GP → compute UCB + EI → pick ensemble winner
7. Duplicate check → format as submission string

---

## Notebook Pattern
Each module has one notebook: `module-NN/notebooks/Module_NN_WeekM_Capstone.ipynb`
Single function `analyse_function_wN(fn_id, ...)` handles all 8 functions.

---

## Key Lessons (do not repeat these mistakes)
- W2: Aggressive UCB on F4 → -26.59 (outlier — remove before GP fit)
- W3: High beta + SVM region classification → 0/8 improved. Never use SVM as region filter again.
- W4+: Trust regions essential. Always anchor to all-time best X, not GP best.
- Boundary corners [0,0,...] and [1,1,...] consistently bad — clip to [0.02, 0.98].

---

## How to Use This File Efficiently
When starting a new week, paste ONLY:
```
Module NN results: F1=X, F2=X, F3=X, F4=X, F5=X, F6=X, F7=X, F8=X
Generate Week M submissions.
```
Claude will use this CLAUDE.md as full context — no need to re-explain the project.
