@echo off
goto start
:start
cd %~dp0
set "name=PCID Fix"
goto compile
:compile
cls
pyinstaller --onefile --windowed --uac-admin "%name%.py"
echo Press any key to exit
pause>nul
exit
