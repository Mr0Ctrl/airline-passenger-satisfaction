# AI Agent Instructions (`AGENTS.md`)

This repository is a **4-person academic data mining project** (COM4569/CMP4569, Ankara University) predicting airline passenger satisfaction.

## Non-Negotiable Rules
1. **Respect Stage Isolation**: Each pipeline stage lives in its own notebook (`notebooks/01_eda.ipynb` through `06_evaluation_reporting.ipynb`). Only modify the notebook(s) relevant to your assigned task.
2. **Follow Artifact Contracts**: Read inputs and write outputs strictly according to `docs/PIPELINE_SPEC.md` (creating output directories with `mkdir(parents=True, exist_ok=True)` as needed).
3. **Reproducibility**: Always use `RANDOM_STATE = 42` and `N_SPLITS = 5`. Fit all imputers, scalers, encoders, and feature selectors **only on the training split** (`train.csv` / `X_train_*`).
4. **Cross-Platform Compatibility**: Never hardcode OS-specific paths or `/` vs `\` separators. Always use `pathlib.Path`.
5. **Git Hygiene**: Never commit files in `data/raw/`, `data/processed/`, `data/features/`, `.venv/`, or `models/**/*.joblib`. Commit meaningful milestones with Conventional Commits (`docs/GIT_WORKFLOW.md`).

## Essential References
- Project roadmap & team roles: `docs/DEVELOPMENT_PLAN.md`
- Stage I/O contracts & schemas: `docs/PIPELINE_SPEC.md`
- Git branching & commit rules: `docs/GIT_WORKFLOW.md`
- Detailed AI session handoff guide: `docs/AI_SESSION_GUIDE.md`
