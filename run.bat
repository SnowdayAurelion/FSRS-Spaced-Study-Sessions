@echo off
call venv\Scripts\activate
python main.py
set exit_code=%errorlevel%
if %exit_code% neq 0 (
    pause
)