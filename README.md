# Imperial-AIML-Capstone


# 🚀  Bayesian Black-Box Optimisation — Capstone Project

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Type](https://img.shields.io/badge/Type-Capstone-green)
![Modules](https://img.shields.io/badge/Modules-12--24-purple)

## 📄 Overview
This project is the Capstone requirement for the Imperial College 
AI/ML programme, running from Module 12 through to Module 24.

The challenge involves optimising 8 unknown black-box functions 
of increasing dimensionality (2D to 8D) using a limited number 
of weekly queries. Each week, one new input point per function 
is submitted via the capstone portal, and the resulting output 
is used to refine the search strategy.

The goal is to find the input that maximises the output of each 
function through intelligent, iterative, data-driven decisions — 
reflecting how optimisation is approached in real-world ML research.

## ❓ Problem Statement
Eight synthetic black-box functions are provided, each simulating 
a real-world optimisation challenge such as radiation detection, 
drug discovery, or hyperparameter tuning. The internal equations 
are unknown — only inputs and outputs are observable.

Each function must be maximised using limited weekly queries, 
making smart search strategy essential.

## 🎯 Project Goals
The primary objectives of this analysis are:
1. **Explore** unknown function landscapes intelligently
2. **Exploit** promising regions as data grows each week
3. **Iterate** and refine strategy based on weekly results
4. **Reflect** on approach and document decision-making throughout

## 📊 Functions Overview
| Function | Dimensions | Description |
|---|---|---|
| F1 | 2D | Radiation Detection |
| F2 | 2D | Noisy ML Model |
| F3 | 3D | Drug Discovery |
| F4 | 4D | Warehouse Placement |
| F5 | 4D | Chemical Yield |
| F6 | 5D | Cake Recipe Optimisation |
| F7 | 6D | ML Hyperparameter Tuning |
| F8 | 8D | Complex 8D Optimisation |

## 🛠️ Technologies Used
| Category | Technologies |
| :--- | :--- |
| **Language** | Python |
| **Libraries** | NumPy, Matplotlib, Scikit-Learn, SciPy |
| **Models** | Gaussian Process and other surrogate models |
| **Tools** | Jupyter Notebooks, Git, GitHub |

## 🗓️ Module Progress
| Module | Week | Status | Strategy Used |
|---|---|---|---|
| Module 12 | Week 1 | ✅ Complete | GP + UCB (adaptive beta) |
| Module 13 | Week 2 | ⏳ Coming soon | TBD |
| Module 14 | Week 3 | ⏳ Coming soon | TBD |
| Module 15 | Week 4 | ⏳ Coming soon | TBD |

## 📁 Repository Structure
```
imperial-aiml-capstone/
│
├── README.md
│
├── module-12/
│   ├── notebook.ipynb
│   └── plots/
│
├── module-13/
│   ├── notebook.ipynb
│   └── plots/
│
└── ...
```

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
   jupyter notebook module-12/notebook.ipynb
```
```
