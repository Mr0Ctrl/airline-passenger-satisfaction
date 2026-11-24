"""Cross-platform Kaggle dataset downloader for Airline Passenger Satisfaction."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

DATASET_SLUG = "teejmahal20/airline-passenger-satisfaction"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
EXPECTED_FILES = ("train.csv", "test.csv")


def _all_present() -> bool:
    return all((RAW_DIR / name).is_file() for name in EXPECTED_FILES)


def _copy_csvs_from(src_dir: Path) -> bool:
    found = False
    for csv_file in src_dir.rglob("*.csv"):
        target_name = csv_file.name.lower()
        if target_name in EXPECTED_FILES:
            shutil.copy2(csv_file, RAW_DIR / target_name)
            found = True
    return found and _all_present()


def _download_via_kagglehub() -> bool:
    try:
        import kagglehub  # type: ignore

        print(f"Downloading '{DATASET_SLUG}' via kagglehub...")
        cached_path = Path(kagglehub.dataset_download(DATASET_SLUG))
        return _copy_csvs_from(cached_path)
    except Exception as exc:
        print(f"kagglehub download failed: {exc}")
        return False


def _download_via_kaggle_cli() -> bool:
    kaggle_exe = shutil.which("kaggle")
    if not kaggle_exe:
        print("kaggle CLI not found on PATH.")
        return False

    print(f"Downloading '{DATASET_SLUG}' via kaggle CLI...")
    try:
        subprocess.run(
            [
                kaggle_exe,
                "datasets",
                "download",
                "-d",
                DATASET_SLUG,
                "-p",
                str(RAW_DIR),
                "--unzip",
            ],
            check=True,
        )
        return _all_present()
    except subprocess.CalledProcessError as exc:
        print(f"kaggle CLI download failed: {exc}")
        return False


def _validate_files() -> None:
    import pandas as pd

    for name in EXPECTED_FILES:
        path = RAW_DIR / name
        df = pd.read_csv(path, nrows=5)
        total_rows = sum(1 for _ in path.open("r", encoding="utf-8")) - 1
        print(f"Verified {path.relative_to(PROJECT_ROOT)}: {total_rows:,} rows, {len(df.columns)} columns")


def main() -> int:
    parser = argparse.ArgumentParser(description="Download Airline Passenger Satisfaction dataset.")
    parser.add_argument("--force", action="store_true", help="Re-download even if files already exist.")
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if _all_present() and not args.force:
        print("Dataset files already present in data/raw/. Use --force to re-download.")
        _validate_files()
        return 0

    if _download_via_kagglehub() or _download_via_kaggle_cli():
        _validate_files()
        return 0

    print("\n[ACTION REQUIRED] Automated Kaggle download could not complete.")
    print("Please either:")
    print("  1. Configure Kaggle API credentials (~/.kaggle/kaggle.json on Linux/macOS")
    print("     or %USERPROFILE%\\.kaggle\\kaggle.json on Windows) and re-run:")
    print("       python scripts/download_data.py --force")
    print(f"  2. Or manually download from: https://www.kaggle.com/datasets/{DATASET_SLUG}")
    print(f"     and place train.csv & test.csv into: {RAW_DIR}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
