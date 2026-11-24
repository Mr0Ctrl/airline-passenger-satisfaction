@echo off
setlocal enabledelayedexpansion

cd /d "%~dp0"

echo === Airline Passenger Satisfaction: Windows CMD Setup ===

where py >nul 2>nul
if %errorlevel%==0 (
    set "PY_CMD=py -3"
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        set "PY_CMD=python"
    ) else (
        echo Error: Python 3.10+ was not found on PATH.
        exit /b 1
    )
)

if not exist ".venv" (
    echo [1/4] Creating virtual environment in .venv ...
    %PY_CMD% -m venv .venv
    if errorlevel 1 exit /b 1
) else (
    echo [1/4] Using existing .venv ...
)

echo [2/4] Upgrading pip and installing requirements ...
".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 exit /b 1
".venv\Scripts\pip.exe" install -r requirements.txt
if errorlevel 1 exit /b 1

echo [3/4] Registering Jupyter kernel (airline-dm) ...
".venv\Scripts\python.exe" -m ipykernel install --user --name airline-dm --display-name "Python (airline-dm)"
if errorlevel 1 exit /b 1

echo [4/4] Downloading dataset to data\raw\ ...
".venv\Scripts\python.exe" scripts\download_data.py
if errorlevel 1 exit /b 1

echo.
echo Setup complete! Activate the environment with:
echo   .venv\Scripts\activate
endlocal
