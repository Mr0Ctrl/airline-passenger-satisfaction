#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

echo "=== Airline Passenger Satisfaction: Linux/macOS Setup ==="

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: python3 is not installed. Please install Python 3.10+ first."
    exit 1
fi

if [ ! -d ".venv" ]; then
    echo "[1/4] Creating virtual environment in .venv ..."
    python3 -m venv .venv
else
    echo "[1/4] Using existing .venv ..."
fi

echo "[2/4] Upgrading pip and installing requirements ..."
.venv/bin/python -m pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

echo "[3/4] Registering Jupyter kernel (airline-dm) ..."
.venv/bin/python -m ipykernel install --user --name airline-dm --display-name "Python (airline-dm)"

echo "[4/4] Downloading dataset to data/raw/ ..."
.venv/bin/python scripts/download_data.py

echo ""
echo "Setup complete! Activate the environment with:"
echo "  source .venv/bin/activate"
