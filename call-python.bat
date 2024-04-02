@echo off
setlocal

call venv\Scripts\activate.bat

pythonw.exe main.py %*