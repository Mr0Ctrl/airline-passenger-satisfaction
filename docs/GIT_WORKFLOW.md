# Git Workflow & Team Collaboration Guide

## 1. Branching Strategy
- `main`: Always stable, tested, milestone-ready code. Direct pushes are discouraged after initial setup.
- `dev`: Integration branch where completed stage branches are merged and verified together.
- `feature/<stage>-<short-desc>`: Personal working branches, one per task/notebook.
  - Examples:
    - `feature/01-eda-berhan`
    - `feature/02-preprocessing-berhan`
    - `feature/03-feature-selection-ahmet`
    - `feature/05-lgbm-tuning-mehmet`

---

## 2. Avoiding Notebook Merge Conflicts
1. **One owner per notebook at a time**: Never edit a notebook owned by another stage without coordinating.
2. **Keep stages self-contained**: Read inputs from `data/` and write outputs to `data/`, `models/`, or `reports/` using `Path.mkdir(parents=True, exist_ok=True)`.
3. **Never commit data or virtual environments**: `.gitignore` excludes `data/raw/*.csv`, `data/processed/*.parquet`, `data/features/*.parquet`, `models/**/*.joblib`, and `.venv/`.
4. **Milestone outputs**: Export charts to `reports/figures/` and metrics to `reports/metrics/` so reviewers can inspect results without parsing raw `.ipynb` diffs.

---

## 3. Conventional Commits
Use clear, atomic commit messages following Conventional Commits:
- `feat(stage-02): implement grouped median imputation and encoding`
- `feat(stage-03): add mutual information and RFE feature selection`
- `model(stage-05): tune LightGBM hyperparameters with 5-fold CV`
- `docs: update pipeline specification with feature schema`
- `fix(scripts): handle missing kaggle credentials gracefully`
- `chore: update requirements.txt`

---

## 4. Milestone Tagging
Tag `main` after each phase passes end-to-end verification:
- `v0.1-setup` — Environment, setup scripts, folder structure, and docs
- `v0.2-eda` — Completed EDA & figures
- `v0.3-preprocessing` — Verified processed Parquet artifacts
- `v0.4-features` — Verified Full vs. Reduced feature sets
- `v0.5-baseline` — 5-Fold CV & Logistic Regression baseline
- `v0.6-models` — Tuned Random Forest & LightGBM/CatBoost
- `v1.0-final` — Final evaluation, report tables, and presentation-ready repo
