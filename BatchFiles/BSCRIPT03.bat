@ECHO OFF

:starter
cls
echo -~-~-~-~-~-~-~-~-~-~-~-~-~-~
echo   Hello! What do you need?
echo   1) IP Configuration
echo   2) Task Manager
echo   3) Check Disk
echo   4) Format Disk
echo   5) Defrag Disk
echo   6) Find Something
echo   7) Attribute Stuff
echo   8) Goodbye
echo -~-~-~-~-~-~-~-~-~-~-~-~-~-~

choice /c 12345678 /n
if errorlevel 8 goto byebye
if errorlevel 7 goto attribution
if errorlevel 6 goto finders
if errorlevel 5 goto defragg
if errorlevel 4 goto formatting
if errorlevel 3 goto diskstat
if errorlevel 2 goto seetask
if errorlevel 1 goto ipcfigure


:ipcfigure
cls
ipconfig
echo.
pause
goto starter


:seetask
cls
echo -~-~-~-~-~-~-~-~-~-~-~-~-~-~
echo   1) Check Task List
echo   2) Kill A Task
echo   3) Back
echo -~-~-~-~-~-~-~-~-~-~-~-~-~-~
choice /c 123 /n
if errorlevel 3 goto starter
if errorlevel 2 goto kill
if errorlevel 1 goto cqr

:cqr
cls
tasklist
echo.
pause
goto seetask

:kill
cls
set /p pid="What is the PID of the target? > "
echo I see..
echo.
taskkill /pid %pid% /f
if not errorlevel 1 echo Pleasure doing business.
if errorlevel 1 echo Apologies.
echo.
pause
goto seetask


:diskstat
cls
set /p dvchk="Which drive are we checking? > "
echo Alright! Checking Drive %dvchk%:!
echo.
chkdsk %dvchk%:
if errorlevel 1 echo Uh, seems like I can't check it right now sorry.
echo.
pause
goto starter


:formatting
cls
echo WARNING! Formatting means DELETING all data from this drive. Are you sure?
echo [1] Yes
echo [2] No

choice /c 12 /n
echo -~-~-~-~-~-~-~-~-~-~-~-~-~-~
if errorlevel 2 goto formatno
if errorlevel 1 goto formatyes

:formatno
echo Good call! Let's go back.
echo.
pause
goto starter

:formatyes
set /p dvfor="Sure okay! Which drive are we formatting? > "
echo Alright! Formatting Drive %dvfor%:!
echo.
format %dvfor%: /q
if errorlevel 1 echo Uh, seems like I can't format it right now sorry.
echo.
pause
goto starter


:defragg
cls
set /p dvfrg="Which drive are we defragging? > "
echo Alright! Formatting Drive %dvfrg%:!
echo.
defrag %dvfrg%: /u
if errorlevel 1 echo Uh, seems like I can't defrag it right now sorry.
echo.
pause
goto starter

:finders
cls
set /p search="What string are we looking for? > "
set /p findir="Okay, but where is the file located? (Example: C:\Documents\text.txt) > "
echo.
echo Okay let's see here...
echo.
find /i /n "%search%" %findir%
echo.
echo Okay, that's all!
pause
goto starter

:attribution
cls
set /p attfil="Give me the full directory of the file > "
echo Hmmm...

:attstart
cls
echo -~-~-~-~-~-~-~-~-~-~-~-~-~-~
echo ATTR: %attfil%
echo -~-~-~-~-~-~-~-~-~-~-~-~-~-~
echo   1) Display Attributes
echo   2) Add Attribute
echo   3) Remove Attribute
echo   4) Back
echo -~-~-~-~-~-~-~-~-~-~-~-~-~-~
choice /c 1234 /n
if errorlevel 4 goto starter
if errorlevel 3 goto attdel
if errorlevel 2 goto attadd
if errorlevel 1 goto attdisplay

:attdisplay
cls
attrib "%attfil%"
echo.
pause
goto attstart

:attadd
cls
set /p addtribute="What attribute do we add? (H, R, S etc.) > "
echo.
echo Alright! I'll add those!
echo.
pause
attrib +%addtribute% "%attfil%"
goto attstart

:attdel
cls
set /p addtribute="What attribute do we remove? (H, R, S etc.) > "
echo.
echo Alright! I'll remove those!
echo.
pause
attrib -%addtribute% "%attfil%"
goto attstart


:byebye
cls
echo Ohh, see ya later!
echo.
pause
exit