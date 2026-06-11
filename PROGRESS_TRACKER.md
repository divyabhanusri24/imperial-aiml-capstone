# Progress Tracker — BBO Capstone

> Update this after every weekly portal result comes back. One row per function per week.

## All-Time Best Per Function (as of W8 submitted)
| F | Best Output | Best X | Week |
|---|------------|--------|------|
| F1 | 0.0880 | 0.653384-0.652924 | W6 |
| F2 | 0.6478 | 0.704856-0.921380 | W6 |
| F3 | -0.0107 | 0.020584-0.969910-0.474761 | W1 |
| F4 | -0.1284 | 0.352971-0.651614-0.805417-0.616108 | W4 |
| F5 | **3632.18** | 0.044074-0.979912-0.978237-0.978721 | **W8** |
| F6 | **-0.2037** | 0.409346-0.360704-0.502905-0.718263-0.020264 | **W8** |
| F7 | **2.7440** | 0.138618-0.329866-0.325614-0.264255-0.295279-0.651123 | **W8** |
| F8 | 9.9275 | 0.089787-0.068251-0.180968-0.327284-0.766207-0.653365-0.174832-0.499246 | W5 |

---

## Week-by-Week Results

### Week 1 (Module 12)
| F | Submitted X | Result | vs Prior Best | Note |
|---|------------|--------|--------------|------|
| F1 | — | — | — | Broad GP+UCB exploration |
| F2 | — | — | — | |
| F3 | — | -0.011 | ✅ Best | |
| F4 | — | — | — | |
| F5 | — | — | — | |
| F6 | — | -0.361 | ✅ Best | |
| F7 | — | — | — | |
| F8 | — | — | — | |
**Summary:** 6/8 improved

### Week 2 (Module 13)
| F | Submitted X | Result | vs Prior Best | Note |
|---|------------|--------|--------------|------|
| F1 | 0.591000-0.591000 | 2.82e-04 | ✅ Best | |
| F2 | 0.703000-0.927000 | 0.611 | (= Initial) | |
| F3 | — | — | — | |
| F4 | — | -26.59 | ❌ Outlier | Remove from GP fit! |
| F5 | — | — | — | |
| F6 | — | — | — | |
| F7 | — | — | — | |
| F8 | — | — | — | |
**Summary:** 1/8 improved (F1)

### Week 3 (Module 14) — GP+UCB+SVM disaster
| F | Submitted X | Result | vs Prior Best | Note |
|---|------------|--------|--------------|------|
| F1 | — | — | ❌ | |
| F2 | — | — | ❌ | |
| F3 | — | — | ❌ | |
| F4 | — | -26.07 | ❌ Outlier | Remove from GP fit! |
| F5 | — | — | ❌ | |
| F6 | — | — | ❌ | |
| F7 | — | — | ❌ | |
| F8 | — | — | ❌ | |
**Summary:** 0/8 improved — SVM region filter failed

### Week 4 (Module 15) — Trust regions + EI ensemble
| F | Submitted X | Result | vs Prior Best | Note |
|---|------------|--------|--------------|------|
| F1 | — | — | — | |
| F2 | — | — | — | |
| F3 | — | — | — | |
| F4 | — | -0.128 | ✅ Best | First real improvement |
| F5 | 0.241041-0.805036-0.948951-0.905090 | 2496.35 | ✅ Best ⭐ | Massive jump |
| F6 | — | — | — | |
| F7 | — | 2.671 | ✅ Best | |
| F8 | — | 9.897 | ✅ Best | |
**Summary:** 4/8 improved (F4, F5, F7, F8)

### Week 5 (Module 16)
| F | Submitted X | Result | vs Prior Best | Note |
|---|------------|--------|--------------|------|
| F1 | 0.580092-0.683225 | 8.11e-05 | ❌ | |
| F2 | 0.702813-0.926626 | 0.5834 | ❌ | |
| F3 | 0.365086-0.316421-0.471038 | -0.0187 | ❌ | |
| F4 | 0.344700-0.645505-0.791987-0.622463 | -13.98 | ❌ | Regression |
| F5 | 0.139557-0.911522-0.979905-0.977049 | 2941.85 | ✅ | W4 best beaten |
| F6 | 0.417831-0.356959-0.468069-0.668531-0.039515 | -0.2999 | ✅ Best | |
| F7 | 0.384097-0.122113-0.444891-0.357064-0.147383-0.783086 | 1.6608 | ❌ | |
| F8 | 0.089787-0.068251-0.180968-0.327284-0.766207-0.653365-0.174832-0.499246 | 9.9275 | ✅ Best | |
**Summary:** 3/8 improved (F5, F6, F8)

### Week 6 (Module 17)
| F | Submitted X | Result | vs Prior Best | Note |
|---|------------|--------|--------------|------|
| F1 | 0.653384-0.652924 | 0.0880 | ✅ Best | Big jump! |
| F2 | 0.704856-0.921380 | 0.6478 | ✅ Best | |
| F3 | 0.151659-0.826046-0.622768 | -0.0868 | ❌ | |
| F4 | 0.291709-0.714786-0.911879-0.664486 | -21.25 | ❌ | Regression |
| F5 | 0.102387-0.951309-0.977662-0.978193 | 3303.92 | ✅ | |
| F6 | 0.394360-0.399099-0.411100-0.595076-0.020599 | -0.5181 | ❌ | |
| F7 | 0.027785-0.208441-0.270801-0.266138-0.195016-0.698660 | 2.1498 | ❌ | |
| F8 | 0.029320-0.285338-0.223021-0.041430-0.625367-0.719031-0.033888-0.797446 | 9.8116 | ❌ | |
**Summary:** 3/8 improved (F1, F2, F5)

### Week 7 (Module 18)
| F | Submitted X | Result | vs Prior Best | Note |
|---|------------|--------|--------------|------|
| F1 | 0.533625-0.533688 | 3.88e-13 | ❌ | Big drop |
| F2 | 0.702665-0.919352 | 0.6476 | ❌ | Near plateau |
| F3 | 0.267218-0.472728-0.513126 | -0.0384 | ❌ | |
| F4 | 0.341374-0.485949-0.606273-0.478470 | -4.94 | ❌ | Still volatile |
| F5 | 0.071951-0.977037-0.979767-0.979593 | 3626.83 | ✅ Best | Upward trend! |
| F6 | 0.441360-0.279908-0.514886-0.684556-0.020780 | -0.3390 | ❌ | Regression |
| F7 | 0.255243-0.272333-0.253655-0.238536-0.237243-0.658362 | 2.5916 | ❌ | |
| F8 | 0.306263-0.307104-0.109816-0.361473-0.669399-0.417361-0.175248-0.274400 | 9.8171 | ❌ | |
**Summary:** 1/8 improved (F5 only)

### Week 8 (Module 19) — Submitted, awaiting results
| F | Submitted X | Result | vs Prior Best | Strategy |
|---|------------|--------|--------------|---------|
| F1 | 0.643797-0.704343 | -0.000114 | ❌ | MOMENTUM, r=0.06 — moved too far |
| F2 | 0.703797-0.924514 | 0.6409 | ❌ | Near plateau |
| F3 | 0.100454-0.240875-0.185908 | -0.1415 | ❌ | Full LHS failed again |
| F4 | 0.383806-0.511512-0.656499-0.491038 | -7.163 | ❌ | Volatile |
| F5 | 0.044074-0.979912-0.978237-0.978721 | **3632.18** | ✅ NEW BEST | Upward trend! |
| F6 | 0.409346-0.360704-0.502905-0.718263-0.020264 | **-0.2037** | ✅ NEW BEST | Big jump |
| F7 | 0.138618-0.329866-0.325614-0.264255-0.295279-0.651123 | **2.7440** | ✅ NEW BEST | Recovery working |
| F8 | 0.182189-0.037358-0.268170-0.170921-0.585250-0.468337-0.247759-0.632930 | 9.887 | ❌ | Slight drop |
**Summary:** 3/8 improved (F5, F6, F7)

### Week 9 (Module 20) — Ready to submit
| F | Suggested X | Strategy |
|---|------------|---------|
| F1 | GP output (trust r=0.03 around W6 best 0.653384-0.652924) | RECOVERY — x2 must stay near 0.653, NOT pushed to 0.70+ |
| F2 | GP output (trust r=0.03 around W6 best 0.704856-0.921380) | PLATEAU — hold x2 near 0.921, push x1 slightly |
| F3 | GP output (trust r=0.12 around W1 best 0.020584-0.969910-0.474761) | ANCHOR — W8 worst ever, return to W1 region |
| F4 | GP output (trust r=0.06 around W4 best 0.352971-0.651614-0.805417-0.616108) | TIGHT RECOVERY — tighter than W8, exclude W2/W3 outliers |
| F5 | GP output (trust r=0.02 around W8 best 0.044074-0.979912-0.978237-0.978721) | MOMENTUM — continue x1 downward, keep x2-x4 at 0.979-0.980 |
| F6 | GP output (trust r=0.06 around W8 best 0.409346-0.360704-0.502905-0.718263-0.020264) | MOMENTUM — x5 small, x4 trending up |
| F7 | GP output (trust r=0.10 around W8 best 0.138618-0.329866-0.325614-0.264255-0.295279-0.651123) | MOMENTUM — upward trend continuing |
| F8 | GP output (trust r=0.12 around W5 best 0.089787-0.068251-0.180968-0.327284-0.766207-0.653365-0.174832-0.499246) | RECOVERY — 3 weeks since beating W5, go tight |

---

## Remaining Weeks
- Week 9 → Module 20
- Week 10 → Module 21
- Week 11 → Module 22
- Week 12 → Module 23
- Week 13 → Module 24 (Final)

---

## F4 Outliers to Always Exclude from GP Fit
- W2: -26.59
- W3: -26.07
