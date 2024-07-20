@ECHO OFF

echo This program will sort all the text files inside the
echo  C: directory and archive it to Z:\Archive.
echo.
pause

set srcDir=C:\
md Z:\Archive
set archDir=Z:\Archive

for /f "tokens=*" %%a in ('dir %srcDir%\*.txt /b /o:-d') do echo %%a

for /f "tokens=*" %%a in ('forfiles /p %srcDir% /m *.txt /d -30 /c "cmd /c echo @path"') do move "%%a" %archDir%

echo So there are the largest archived files:
set count=0
for /f "tokens=*" %%a in ('dir %archDir%\*.txt /b /s /o:-s') do (
    set /a count+=1
    echo !count!. %%a
    if !count! geq 5 (
        echo.
        choice /c 123 /n /m "Shall we delete these old, large files? (1. Yes, 2. No): "
        if errorlevel 1 (
            del "%%a"
            echo Alright. Deleted %%a!
        ) else (
            echo Okay, files will be retained!
            goto end
        )
    )
)


:end
pause
exit