@ECHO OFF

:starter
cls
echo -~-~-~-~-~-~-~-~-~-~-~-~-~
echo   Welcome! Pick a shape:
echo   1) CIRCLE
echo   2) TRIANGLE
echo   3) QUARILATERAL
echo -~-~-~-~-~-~-~-~-~-~-~-~-~

choice /c 123 /n
if errorlevel 3 goto quad
if errorlevel 2 goto triad
if errorlevel 1 goto noad



:noad
cls
set radius=0
set pi=3.141592653589793238462643383279502884197
set /p radius="What is the radius of your circle? > "
if %radius%==0 goto nothingc
set /a nostatearea=pi*radius*radius
echo.

echo Wow! The area of your circle is %nostatearea% units! That is ginormous!
echo.

pause
goto starter



:triad
cls
set matches=0
set tristate=SCALENE

set tone=0
set ttwo=0
set ttre=0

set /p tone="How long is the first side of your triangle? > "
set /p ttwo="Hm, how about the next side of your triangle? > "
set /p ttre="Ohh ok, now how about the last side, how long? > "

if %tone%==0 goto nothingt
if %ttwo%==0 goto nothingt
if %ttre%==0 goto nothingt

for %%i in (%ttwo% %ttre%) do if %tone%==%%i set /a matches+=1
if %matches%==0 if %ttwo%==%ttre% set /a matches+=1

if %matches%==2 set tristate=EQUILATERAL
if %matches%==1 set tristate=ISOSCELES

set /a tonesqr=tone*tone
set /a ttwosqr=ttwo*ttwo
set /a ttresqr=ttre*ttre

set /a absum=tonesqr+ttwosqr
set /a bcsum=ttwosqr+ttresqr
set /a acsum=tonesqr+ttresqr

if %absum%==%ttresqr% set tristate=RIGHT
if %bcsum%==%tonesqr% set tristate=RIGHT
if %acsum%==%ttwosqr% set tristate=RIGHT
echo.

echo Wow! That's a nice %tristate% triangle you got there! Splendid!
echo.

pause
goto starter



:quad
cls
set qtype=NONE
set height=0
set width=0
set /p height="How high is your quarilateral? > "
set /p width="Okay, now, how wide is your quarilateral? > "
set /a quadstatearea=height*width

if %height%==0 goto nothings
if %width%==0 goto nothings
if %height%==%width% set qtype=SQUARE
if not %height%==%width% set qtype=RECTANGLE
echo.

echo Wow! The area of your %qtype% is %quadstatearea% units! That is amazing!
echo.

pause
goto starter



:nothingc
echo.

echo Wow! That adds up to nothing! That is ginormous!
echo.

pause
goto starter



:nothingt
echo.

echo Wow! That's a nice lack of something you got there! Splendid!
echo.

pause
goto starter


:nothings
echo.

echo Wow! That adds up to nothing! That is amazing!
echo.

pause
goto starter