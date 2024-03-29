@echo off

cd "%~dp0"

call env\Scripts\activate

python main.py

call env\Scripts\deactivate.bat
