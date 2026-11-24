$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectRoot

Write-Host "=== Airline Passenger Satisfaction: Windows PowerShell Setup ==="

$PyCmd = $null
if (Get-Command py -ErrorAction SilentlyContinue) {
    $PyCmd = @("py", "-3")
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $PyCmd = @("python")
} else {
    Write-Error "Python 3.10+ was not found on PATH."
    exit 1
}

if (-not (Test-Path ".venv")) {
    Write-Host "[1/4] Creating virtual environment in .venv ..."
    if ($PyCmd.Length -eq 2) {
        & $PyCmd[0] $PyCmd[1] -m venv .venv
    } else {
        & $PyCmd[0] -m venv .venv
    }
} else {
    Write-Host "[1/4] Using existing .venv ..."
}

$VenvPython = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
$VenvPip = Join-Path $ProjectRoot ".venv\Scripts\pip.exe"

Write-Host "[2/4] Upgrading pip and installing requirements ..."
& $VenvPython -m pip install --upgrade pip
& $VenvPip install -r requirements.txt

Write-Host "[3/4] Registering Jupyter kernel (airline-dm) ..."
& $VenvPython -m ipykernel install --user --name airline-dm --display-name "Python (airline-dm)"

Write-Host "[4/4] Downloading dataset to data\raw\ ..."
& $VenvPython "scripts\download_data.py"

Write-Host ""
Write-Host "Setup complete! Activate the environment with:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
