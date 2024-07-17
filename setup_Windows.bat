@echo off

IF NOT EXIST "venv\Scripts\activate" (
    echo Virtual environment not found, creating one...
    python -m venv venv
)

call venv\Scripts\activate
pip install -r requirements.txt

if %errorlevel% neq 0 pause