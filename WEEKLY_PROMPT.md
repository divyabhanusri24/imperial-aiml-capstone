# Weekly Prompt Templates — Save Your Credits!

> Copy-paste the right template each week. Claude reads CLAUDE.md automatically for full context.
> NEVER paste the whole README or notebook — use these short prompts instead.

---

## Template 1 — New Week Submissions (most common)

```
Week [N] results back:
F1=[output], F2=[output], F3=[output], F4=[output],
F5=[output], F6=[output], F7=[output], F8=[output]

Generate Week [N+1] submission strings for all 8 functions.
Use strategy from CLAUDE.md. Update best results if improved.
```

**Example:**
```
Week 5 results back:
F1=1.2e-04, F2=0.590, F3=-0.009, F4=-0.115, F5=2498.1, F6=-0.340, F7=2.680, F8=10.1

Generate Week 6 submission strings for all 8 functions.
Use strategy from CLAUDE.md. Update best results if improved.
```

---

## Template 2 — Debug a Specific Function

```
F[N] not improving for [X] weeks. All submissions and results:
[paste only the 5-10 rows for that function]

Suggest a different strategy for F[N] next week.
```

---

## Template 3 — Start a New Module Notebook

```
Create Module [NN] Week [N] notebook.
Copy the analyse_function template from module-[MM]/notebooks/.
Update weekly data to include Week [N-1] result: F[k]=[output].
Target: Week [N] submissions.
```

---

## Template 4 — Explain a Concept (no project context needed)

```
Explain [concept] as it applies to Bayesian optimisation.
Give a concrete example with numbers.
```

**Examples of concepts to ask about:**
- UCB acquisition function and beta tuning
- Expected Improvement vs UCB trade-offs
- Why trust regions help in high dimensions
- Latin Hypercube Sampling vs random sampling
- Why GPs struggle beyond ~20 observations in 8D (curse of dimensionality)
- Matérn vs RBF kernel — when to use each

---

## Template 5 — Final Week Strategy Review

```
Final module approaching. Current best results:
[paste All-Time Best table from PROGRESS_TRACKER.md]

Which functions still have room to improve? Suggest aggressive final-week strategy.
```

---

## What NEVER to paste (wastes credits)
- The full README.md
- Full notebook code (only paste the specific function you need help with)
- Old weekly notebook cells you've already run
- The full REFERENCES.md
- All 8 functions' data when you only need help with 1

---

## Credit-Saving Rules
1. **One question per message.** Don't bundle "explain UCB + fix my code + generate submissions" in one prompt.
2. **Paste only the relevant data.** If F5 is the issue, only share F5's history.
3. **Use CLAUDE.md.** It auto-loads project context — you don't need to re-explain the project.
4. **Ask for code skeletons, not full implementations.** Then fill in the specific values yourself.
5. **Start new sessions** for unrelated questions — old context accumulates and costs credits.
