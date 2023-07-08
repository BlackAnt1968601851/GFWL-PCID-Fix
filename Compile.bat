@echo off
goto start
:start
cd %~dp0
set "name=PCID Fix"
goto compile
:compile
cls
pyinstaller --onefile --windowed "%name%.py"
echo Press any key to exit
pause>nul
exit