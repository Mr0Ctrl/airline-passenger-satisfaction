"""End-to-end Jupyter notebook pipeline runner."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

STAGES: list[tuple[int, str]] = [
    (1, "01_eda.ipynb"),
    (2, "02_preprocessing.ipynb"),
    (3, "03_feature_selection.ipynb"),
    (4, "04_baseline_cv.ipynb"),
    (5, "05_model_tuning.ipynb"),
    (6, "06_evaluation_reporting.ipynb"),
]


def check_notebooks() -> int:
    """Validate that all stage notebooks exist and are valid JSON."""
    missing = []
    for stage_num, filename in STAGES:
        nb_path = NOTEBOOKS_DIR / filename
        if not nb_path.is_file():
            missing.append(str(nb_path.relative_to(PROJECT_ROOT)))
            continue
        try:
            with nb_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if "cells" not in data or "nbformat" not in data:
                print(f"[INVALID] Stage {stage_num}: {filename} missing cells/nbformat")
                return 1
            print(f"[OK] Stage {stage_num}: {filename} ({len(data['cells'])} cells)")
        except json.JSONDecodeError as exc:
            print(f"[INVALID JSON] Stage {stage_num}: {filename}: {exc}")
            return 1

    if missing:
        print(f"Missing notebooks: {', '.join(missing)}")
        return 1
    return 0


def run_stages(start_stage: int, end_stage: int) -> int:
    """Execute notebook stages sequentially using jupyter nbconvert."""
    for stage_num, filename in STAGES:
        if stage_num < start_stage or stage_num > end_stage:
            continue
        nb_path = NOTEBOOKS_DIR / filename
        print(f"\n=== Running Stage {stage_num}: {filename} ===")
        cmd = [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "--inplace",
            str(nb_path),
        ]
        result = subprocess.run(cmd, cwd=PROJECT_ROOT)
        if result.returncode != 0:
            print(f"Stage {stage_num} ({filename}) failed with exit code {result.returncode}.")
            return result.returncode
    print("\nPipeline execution completed successfully.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run or validate the end-to-end notebook pipeline.")
    parser.add_argument("--from", dest="start_stage", type=int, default=1, help="First stage number (1-6).")
    parser.add_argument("--to", dest="end_stage", type=int, default=6, help="Last stage number (1-6).")
    parser.add_argument("--check", action="store_true", help="Validate notebooks without executing them.")
    args = parser.parse_args()

    if args.check:
        return check_notebooks()

    return run_stages(args.start_stage, args.end_stage)


if __name__ == "__main__":
    sys.exit(main())
