@echo off
set REZ_ERRORLEVEL=
if "%OS%" == "Windows_NT" goto WinNT

@REM Credit where credit is due:  we return the exit code despite our
@REM use of setlocal+endlocal using a technique from Bear's Journal:
@REM http://code-bear.com/bearlog/2007/06/01/getting-the-exit-code-from-a-batch-file-that-is-run-from-a-python-program/
@REM and also from a permutation of pl2bat
@REM http://www.informit.com/articles/article.aspx?p=29328&seqNum=5
@REM and py2bat
@REM https://mail.python.org/pipermail/python-list/2000-January/020761.html

:WinNT
setlocal
@REM ensure the script will be executed with the Python it was installed for
set path=%~dp0;%~dp0..;%path%
@REM try the script named as the .bat file in current dir
set scriptname=%~dp0%~n0
python "%scriptname%" %*
endlocal & set REZ_ERRORLEVEL=%ERRORLEVEL%

if NOT "%COMSPEC%" == "%SystemRoot%\system32\cmd.exe" goto returncode
goto endrez

:returncode
exit /B %REZ_ERRORLEVEL%

:endrez
call :returncode %REZ_ERRORLEVEL%
