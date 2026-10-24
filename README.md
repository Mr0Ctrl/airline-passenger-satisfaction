# Airline Passenger Satisfaction & Flight Delay Risk Analysis

## 1. Problem Statement & Motivation
Commercial aviation networks operate under dynamic conditions where flight delays, ground operations, and in-flight service quality directly drive customer retention and operational risk. Predicting whether a passenger will report satisfaction or dissatisfaction based on multi-dimensional flight parameters is a classic high-dimensional tabular classification challenge.

The dataset presents mixed continuous and categorical variables, localized class imbalances, and non-linear interactions (e.g., the combined impact of departure delay, flight distance, and cabin class on customer retention). 

**Objective:** Build an end-to-end data mining pipeline to classify passenger satisfaction and operational risk. The study evaluates systematic data preprocessing, feature encoding, feature selection (comparing performance before vs. after dimensionality reduction), and benchmarks three distinct algorithmic families (Logistic Regression, Random Forest, and LightGBM/CatBoost) using cross-validation.

---

## 2. Dataset & Data Source
- **Official Dataset Name:** Airline Passenger Satisfaction (Kaggle Tabular Benchmark / US Airline Operational Feedback).
- **Scale:** ~130,000 records across 23 attributes (103,904 train / 25,976 test split).
- **Key Features:**
  - *Demographics & Flight Metadata:* Gender, Customer Type (Loyal vs. Disloyal), Age, Type of Travel (Personal vs. Business), Class (Business, Eco, Eco Plus), Flight Distance.
  - *Operational Delays:* Departure Delay in Minutes, Arrival Delay in Minutes.
  - *Service Quality Metrics (Scale 0–5):* In-flight Wi-Fi, Departure/Arrival Convenience, Food/Drink, Gate Location, On-board Service, Seat Comfort, In-flight Entertainment, Baggage Handling, Cleanliness.
- **Target Variable:** Binary Classification (`satisfaction`: `neutral/dissatisfied` vs. `satisfied`).

---

## 3. Data Mining Pipeline Architecture

```
[ Raw Dataset: 130,000 Records ]
                │
                ▼
[ Data Cleaning & Preprocessing ]
   ├── Imputation of Missing Arrival Delay Values (Median / KNN)
   ├── Normalization of Continuous Numerical Attributes (Distance, Delays)
   └── Categorical Encoding (One-Hot for Nominal, Ordinal for Cabin Class)
                │
                ▼
[ Feature Selection Experiment (Course Rubric Requirement) ]
   ├── Configuration A: Full Feature Space (All 22 Predictors)
   └── Configuration B: Reduced Feature Space (Top 10-12 Predictors via Mutual Information / RFE)
                │
                ▼
[ Multi-Model Comparative Benchmark ]
   ├── Model 1 (Linear Baseline): Regularized Logistic Regression
   ├── Model 2 (Tree-Based Bagging): Random Forest Classifier
   └── Model 3 (Gradient Boosting): LightGBM / CatBoost
                │
                ▼
[ Performance Evaluation & Metric Matrix (ROC-AUC, F1, Accuracy, Latency) ]
```

---

## 4. Preprocessing & Feature Selection Strategy

### A. Missing Values & Outliers
- `Arrival Delay in Minutes` contains missing records: Imputed using median statistics grouped by `Class` and `Flight Distance` bins.
- Outlier handling: Highly skewed flight delay attributes are evaluated with logarithmic transformation ($\log(1 + x)$) to stabilize variance.

### B. Feature Selection Protocol (Before vs. After Delta)
To satisfy the mandatory academic rubric, all models are evaluated across two feature tiers:
1. **Full Feature Set:** Training models using all 22 raw and encoded features.
2. **Selected Subspace:** Identifying the most informative predictors using Mutual Information Gain and Random Forest Gini Importance (e.g., isolating key drivers such as `In-flight Wi-Fi service`, `Online boarding`, and `Class_Business`).
3. **Comparative Evaluation:** Measuring accuracy loss vs. inference speedup when reducing the feature count from 22 down to ~10.

---

## 5. Required Model Comparison Matrix

| Algorithmic Class | Model | Library | Primary Function |
| :--- | :--- | :--- | :--- |
| **Linear / Probabilistic Baseline** | Logistic Regression ($L_2$ Regularization) | `scikit-learn` | Establishes the linear separability baseline |
| **Non-Linear Ensemble (Bagging)** | Random Forest Classifier | `scikit-learn` | Captures non-linear thresholds and feature importances |
| **Gradient Boosting** | LightGBM or CatBoost | `lightgbm` / `catboost` | High-efficiency gradient boosted decision tree reference |

---

## 6. Evaluation Metrics & Experimental Setup
- **Validation Strategy:** 5-Fold Stratified Cross-Validation on the training split, evaluated finally on the isolated test set.
- **Metrics:**
  - Accuracy & Balanced Accuracy
  - Precision, Recall, and F1-Score (per class)
  - ROC-AUC (Area Under ROC Curve)
  - Confusion Matrix (evaluating false alarms vs. missed dissatisfaction cases)
  - Wall-clock Training and Prediction Time (evaluating computational cost before and after feature selection)

---

## 7. Team Task Distribution (3–4 Person Setup)
- **Data Engineering:** Dataset exploration, missing value imputation, skewness transformations, and categorical encoding.
- **Feature Selection & Analysis:** Implementing Mutual Information and RFE algorithms; generating feature correlation matrices and before/after comparison tables.
- **Model Training & Hyperparameter Tuning:** Implementing Logistic Regression, Random Forest, and LightGBM models; tuning hyperparameters (tree depth, learning rate, regularization).
- **Evaluation, Reporting & Presentation:** Compiling confusion matrices, ROC curves, writing the final IEEE-format academic report, and structuring presentation slides.
