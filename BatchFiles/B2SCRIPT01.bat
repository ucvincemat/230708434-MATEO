@echo off

:start
set /p time24="Give me a time in 24-hour format? (HH:MM) > "
for /f "tokens=1,2 delims=:" %%a in ("%time24%") do (
    set hour=%%a
    set minute=%%b
)

if %hour% geq 12 (
    if not %hour% == 12 (
        set /a hour=hour-12
    )
    set period=PM
) else (
    if %hour%==00 (
        set hour=12
    )
    set period=AM
)

if %hour% lss 10 (
    set hour=0%hour%
)

echo.
echo That is %hour%:%minute% %period% in 12-hour time! Nice!
pause
cls
goto start