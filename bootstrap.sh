#!/usr/bin/env bash

set -e

echo "=== Browser MCP Bootstrap ==="

# Move to the project directory
cd "$(dirname "$0")"

echo "[1/4] Creating Python virtual environment..."

python3 -m venv .venv

source .venv/bin/activate

echo "[2/4] Installing Python dependencies..."

python -m pip install --upgrade pip
pip install -r requirements.txt

echo "[3/4] Installing Playwright Chromium..."

playwright install chromium

echo "[4/4] Creating required directories..."

mkdir -p screenshots

echo
echo "================================"
echo " Browser MCP is ready."
echo "================================"
echo
echo "Start it with:"
echo
echo "source .venv/bin/activate"
echo "python server.py"
echo
