# AI Session Onboarding & Handoff Guide

Use this guide when starting a new AI coding session on any stage of the project.

---

## 1. Quick Context Check (Run First)
Before writing code in a new session, inspect the current repository state:
1. Read `AGENTS.md` and `docs/PIPELINE_SPEC.md`.
2. Check which stage artifacts already exist:
   - `data/raw/train.csv` and `test.csv`
   - `data/processed/*.parquet`
   - `data/features/*.parquet` and `selected_features.json`
   - `reports/metrics/*.json`
3. Check Git branch and recent commits: `git status && git log -n 5 --oneline`.

---

## 2. Mandatory Academic Rubric Checklist
Ensure any modeling or preprocessing work satisfies all course requirements from `README.md` and `docs/references/Airline Passenger Satisfaction.pdf`:
- [ ] **Missing Values**: `Arrival Delay in Minutes` imputed via grouped median (`Class` + `Flight Distance` bins) — fit on train only.
- [ ] **Skewness**: Evaluate/apply `log1p` on flight delay features.
- [ ] **Encoding**: Ordinal encoding for `Class` (`Eco` < `Eco Plus` < `Business`); One-Hot for nominal (`Gender`, `Customer Type`, `Type of Travel`).
- [ ] **Feature Selection Experiment**: Compare **Full Feature Space** vs. **Reduced Feature Space** (Top 10–12 via Mutual Information + RFE).
- [ ] **3 Algorithmic Families**:
  1. Linear Baseline: Regularized Logistic Regression ($L_2$)
  2. Bagging Ensemble: Random Forest Classifier
  3. Gradient Boosting: LightGBM and/or CatBoost
- [ ] **Validation & Metrics**: 5-Fold Stratified CV on train, final test evaluation recording Accuracy, Balanced Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix, and Train/Predict Latency (`time.perf_counter()`).

---

## 3. Running & Verifying the Pipeline
- Check notebook structure: `python scripts/run_pipeline.py --check`
- Run specific stages: `python scripts/run_pipeline.py --from 2 --to 4`
- Run full end-to-end pipeline: `python scripts/run_pipeline.py`

---

## 4. Session Handoff Protocol
Before ending an AI session:
1. Execute the modified notebook(s) top-to-bottom to confirm zero errors.
2. Verify expected artifacts exist in `data/`, `models/`, or `reports/`.
3. Run `git status` to ensure no data/venv files are staged.
4. Commit milestone progress with a Conventional Commit message (see `docs/GIT_WORKFLOW.md`).
