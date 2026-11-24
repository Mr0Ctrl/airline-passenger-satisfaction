# Pipeline Specification & Artifact Contracts

Every notebook stage reads deterministic inputs from disk and writes deterministic outputs to disk. This decouples team members' work and guarantees end-to-end reproducibility.

---

## Stage Contracts

| Stage | Notebook | Required Inputs | Required Outputs |
| :--- | :--- | :--- | :--- |
| **01** | `01_eda.ipynb` | `data/raw/train.csv`, `data/raw/test.csv` | `reports/figures/eda_*.png`, `reports/tables/eda_summary.csv` |
| **02** | `02_preprocessing.ipynb` | `data/raw/train.csv`, `data/raw/test.csv` | `data/processed/X_train_full.parquet`<br>`data/processed/X_test_full.parquet`<br>`data/processed/y_train.parquet`<br>`data/processed/y_test.parquet`<br>`models/preprocessor.joblib` |
| **03** | `03_feature_selection.ipynb` | `data/processed/X_train_full.parquet`<br>`data/processed/X_test_full.parquet`<br>`data/processed/y_train.parquet` | `data/features/selected_features.json`<br>`data/features/X_train_reduced.parquet`<br>`data/features/X_test_reduced.parquet`<br>`reports/figures/feature_importance.png` |
| **04** | `04_baseline_cv.ipynb` | `data/processed/*`, `data/features/*` | `models/baseline/logreg_full.joblib`<br>`models/baseline/logreg_reduced.joblib`<br>`reports/metrics/baseline_metrics.json` |
| **05** | `05_model_tuning.ipynb` | `data/processed/*`, `data/features/*` | `models/tuned/*.joblib`<br>`reports/metrics/tuned_metrics.json` |
| **06** | `06_evaluation_reporting.ipynb` | `reports/metrics/*.json`<br>`data/processed/*`, `data/features/*` | `reports/tables/model_comparison.csv`<br>`reports/figures/roc_curves.png`<br>`reports/figures/confusion_matrices.png`<br>`reports/figures/latency_comparison.png` |

---

## Target & Metric Schemas

- **Target (`y_train.parquet`, `y_test.parquet`)**: Single column named `satisfaction` with integer values `0` (`neutral or dissatisfied`) and `1` (`satisfied`).
- **Selected Features (`data/features/selected_features.json`)**:
  ```json
  {
    "method": "Mutual Information + RFE",
    "n_features": 10,
    "features": ["Online boarding", "Inflight wifi service", "..."]
  }
  ```
- **Metrics JSON (`reports/metrics/*.json`)**: List of dictionaries (one per model + feature set), each containing:
  `model_name`, `feature_set` (`"full"` or `"reduced"`), `n_features`, `accuracy`, `balanced_accuracy`, `precision`, `recall`, `f1_score`, `roc_auc`, `confusion_matrix`, `train_time_sec`, `predict_time_sec`.
