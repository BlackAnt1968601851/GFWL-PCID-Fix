@echo off
:home
cd %~dp0
set "name=PCID Fix"
title Python Debugger
cls
python.exe "%name%.py"
echo Press any key to exit
pause>nul
exit