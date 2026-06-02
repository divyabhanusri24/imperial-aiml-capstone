# References & Technical Justifications

This document maps each design decision in the BBO capstone to its academic or technical source.

---

## Surrogate Model — Gaussian Process with Matérn Kernel

**Source:** Rasmussen, C.E. & Williams, C.K.I. (2006). *Gaussian Processes for Machine Learning*. MIT Press.

**Justification:** The Matérn ν=2.5 kernel assumes functions are twice differentiable — a reasonable prior for the smooth synthetic landscapes in this challenge. The GP provides calibrated uncertainty estimates out of the box, which is essential for meaningful acquisition function computation.

---

## Acquisition Function — Upper Confidence Bound (UCB)

**Source:** Srinivas, N., Krause, A., Kakade, S., & Seeger, M. (2010). *Gaussian Process Optimization in the Bandit Setting: No Regret and Experimental Design*. ICML.

**Justification:** GP-UCB with adaptive beta controls the exploration-exploitation balance. High beta → explore uncertain regions. Low beta → exploit known-good regions. This paper provides the theoretical grounding for why beta tuning works.

---

## Acquisition Function — Expected Improvement (EI)

**Source:** Jones, D.R., Schonlau, M., & Welch, W.J. (1998). *Efficient Global Optimization of Expensive Black-Box Functions*. Journal of Global Optimization.

**Justification:** EI is framed as "how much do I expect to improve over the current best?" — more conservative than UCB and better suited to exploitation phases. Used in UCB+EI ensemble from Week 4 onwards.

---

## General Bayesian Optimisation Framework

**Source:** Snoek, J., Larochelle, H., & Adams, R.P. (2012). *Practical Bayesian Optimization of Machine Learning Algorithms*. NeurIPS.

**Justification:** Foundational paper establishing GP+EI as the standard framework for optimising expensive black-box functions with limited evaluations. Directly maps to this challenge's setup.

---

## Trust Region Strategy

**Source:** Eriksson, D., Pearce, M., Gardner, J., Turner, R.D., & Poloczek, M. (2019). *Scalable Global Optimization via Local Bayesian Optimization*. NeurIPS. (TuRBO)

**Justification:** With 15–16 observations in 6D–8D spaces, global GP search is unreliable. TuRBO showed that constraining the search to a shrinking neighbourhood around the current best dramatically outperforms global UCB at low observation counts. Implemented from Week 4 as per-function trust radii.

---

## Latin Hypercube Sampling (Candidate Generation)

**Source:** McKay, M.D., Beckman, R.J., & Conover, W.J. (1979). *A Comparison of Three Methods for Selecting Values of Input Variables*. Technometrics.

**Justification:** LHS provides better space coverage than random sampling with the same number of points. Used for generating 50,000 candidate points per function in higher-dimensional search (3D–8D).

---

## Heteroscedastic Noise Modelling (Reference / Future Work)

**Source:** Cowen-Rivers, A.I., et al. (2022). *HEBO: Pushing the Limits of Sample-Efficient Hyperparameter Optimisation*. JAIR. (NeurIPS 2020 BBO Challenge Winner)

**Justification:** HEBO won the NeurIPS 2020 BBO Challenge by modelling spatially varying noise — relevant to F4 which exhibits highly inconsistent outputs across observations. Currently addressing via alpha tuning (GP noise term); HEBO's full heteroscedastic model is a future improvement.

---

## Libraries

| Library | Version | Use | Why Chosen |
|---------|---------|-----|------------|
| scikit-learn | latest | GaussianProcessRegressor, Matérn kernel | Clean GP API, calibrated uncertainty, handles normalize_y automatically |
| scipy | latest | LatinHypercube (qmc), norm (EI) | Standard LHS implementation with reproducible seed |
| numpy | latest | All array operations, log transforms | Core scientific Python stack |
| matplotlib | latest | Weekly progress plots | Standard visualisation |

**Not used:** PyTorch, TensorFlow — deliberate choice. With 15 observations per function, neural network surrogates overfit and lack calibrated uncertainty. GP is the correct tool at this data scale.
