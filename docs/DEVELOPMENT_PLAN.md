# Development Plan — Airline Passenger Satisfaction (COM4569 / CMP4569)

## 1. Project Overview
- **Course:** COM4569 / CMP4569 Data Mining (2026–2027 Fall), Ankara University
- **Goal:** Build a reproducible, field-study-level end-to-end classification pipeline predicting passenger satisfaction (`neutral or dissatisfied` vs. `satisfied`) and benchmarking **Full Feature Space** vs. **Reduced Feature Subspace** across 3 algorithmic families.
- **Dataset:** Kaggle *Airline Passenger Satisfaction* (`teejmahal20/airline-passenger-satisfaction`, ~129,880 records: 103,904 train / 25,976 test, 23 attributes).

---

## 2. Team Roles & Ownership

| Member | Student ID | Primary Pipeline Stages | Notebooks Owned |
| :--- | :--- | :--- | :--- |
| **Berhan Kemal** | 22290679 | Data Preprocessing & Cleaning, Cross-Validation & Baseline | `01_eda.ipynb`, `02_preprocessing.ipynb`, `04_baseline_cv.ipynb` |
| **Ahmet Atakan Demir** | 22290051 | Feature Selection, Evaluation & Reporting | `03_feature_selection.ipynb`, `06_evaluation_reporting.ipynb` |
| **Abdulbarr Salaudeen** | 22290862 | Feature Selection, Model Training & Optimization | `03_feature_selection.ipynb`, `05_model_tuning.ipynb` |
| **Mehmet Özkaya** | 22290513 | Model Training & Optimization, Evaluation & Reporting | `05_model_tuning.ipynb`, `06_evaluation_reporting.ipynb` |

---

## 3. Phased Execution & Milestones

### Phase 0 — Repository, Environment & Pipeline Setup (`v0.1-setup`)
- [x] Cross-platform setup scripts (`setup.sh`, `setup.bat`, `setup.ps1`)
- [x] Automated dataset downloader (`scripts/download_data.py`)
- [x] Template notebooks `01`–`06` and end-to-end runner (`scripts/run_pipeline.py`)
- [x] Governance docs (`DEVELOPMENT_PLAN.md`, `PIPELINE_SPEC.md`, `GIT_WORKFLOW.md`, `AGENTS.md`)

### Phase 1 — Exploratory Data Analysis (`v0.2-eda`)
- **Notebook:** `notebooks/01_eda.ipynb` (Owner: Berhan Kemal)
- **Deliverables:**
  - Missingness audit (`Arrival Delay in Minutes`)
  - Target class balance check
  - Skewness analysis of delays and distance
  - Service quality correlation heatmap exported to `reports/figures/`

### Phase 2 — Data Cleaning & Preprocessing (`v0.3-preprocessing`)
- **Notebook:** `notebooks/02_preprocessing.ipynb` (Owner: Berhan Kemal)
- **Deliverables:**
  - Leakage-free preprocessing pipeline fit **only on `train.csv`**
  - Grouped median imputation for `Arrival Delay in Minutes` (by `Class` and `Flight Distance` bins)
  - `log1p` transformation on skewed delay columns + `StandardScaler`
  - Ordinal encoding (`Class`: `Eco` < `Eco Plus` < `Business`) + One-Hot encoding (`Gender`, `Customer Type`, `Type of Travel`)
  - Outputs saved to `data/processed/` and `models/preprocessor.joblib`

### Phase 3 — Feature Selection Experiment (`v0.4-features`)
- **Notebook:** `notebooks/03_feature_selection.ipynb` (Owners: Ahmet Atakan Demir, Abdulbarr Salaudeen)
- **Deliverables:**
  - Mutual Information Gain ranking + RFE / Random Forest Gini importance
  - Selection of top 10–12 predictors saved to `data/features/selected_features.json`
  - Reduced datasets saved to `data/features/`
  - Feature importance chart in `reports/figures/`

### Phase 4 — 5-Fold Stratified CV & Baseline (`v0.5-baseline`)
- **Notebook:** `notebooks/04_baseline_cv.ipynb` (Owner: Berhan Kemal)
- **Deliverables:**
  - 5-Fold Stratified CV (`RANDOM_STATE=42`)
  - Regularized Logistic Regression ($L_2$) on **Full** and **Reduced** feature sets
  - Standardized JSON metrics saved to `reports/metrics/baseline_metrics.json`

### Phase 5 — Model Training & Hyperparameter Tuning (`v0.6-models`)
- **Notebook:** `notebooks/05_model_tuning.ipynb` (Owners: Mehmet Özkaya, Abdulbarr Salaudeen)
- **Deliverables:**
  - Random Forest Classifier tuned on Full & Reduced feature sets
  - LightGBM (and/or CatBoost) tuned on Full & Reduced feature sets
  - Standardized JSON metrics saved to `reports/metrics/tuned_metrics.json`

### Phase 6 — Final Evaluation, Report & Presentation (`v1.0-final`)
- **Notebook:** `notebooks/06_evaluation_reporting.ipynb` (Owners: Ahmet Atakan Demir, Mehmet Özkaya)
- **Deliverables:**
  - Unified Full vs. Reduced comparison table (`reports/tables/model_comparison.csv`)
  - ROC curves, Confusion Matrices, Latency vs. Accuracy figures (`reports/figures/`)
  - End-to-end verification via `python scripts/run_pipeline.py`
  - Final IEEE-format academic report and presentation slides

---

## 4. Definition of Done (Per Stage)
1. Notebook executes cleanly top-to-bottom (`Restart & Run All` or `scripts/run_pipeline.py`).
2. Expected output artifacts match `docs/PIPELINE_SPEC.md`.
3. `RANDOM_STATE = 42` is used for all stochastic operations.
4. Changes are committed on a feature branch using Conventional Commits and merged via PR into `dev` / `main`.
