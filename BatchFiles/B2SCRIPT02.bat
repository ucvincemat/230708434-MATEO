@echo off
setlocal enabledelayedexpansion

:start
set /p num="Gimme a number > "
echo.

echo Reverse Multiplication Table of %num%
echo ----------------

for /l %%i in (10,-1,1) do (
    set /a result=num*%%i
    echo %num% x %%i = !result!
)
echo ----------------

echo So yeah, that's cool!
pause
cls
goto start