@echo off
WHERE git
IF %ERRORLEVEL% NEQ 0 ECHO Git is required for cloning the repository. If you don't install it, the clone.bat file won't work. 

if not exist "C:\Python34\python.exe" if not exist "C:\Users\Arnym\AppData\Local\Programs\Python\Python36-32\python.exe" (
    goto addtopath
)
echo Python already installed.
goto addtopath

:installpython
echo Installing Python 3.6.4

SET downloadUrl=https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe
SET tempFile=%cd%\.%random%-tmp

echo "Downloading..."

BITSADMIN /transfer /download %downloadUrl% %tempFile% >nul

echo "ok"

start %tempFile%
del %tempFile%

:addtopath
call append_user_path.bat

echo Installing pygame
python -m pip install pygame

echo Installing py2exe
python -m pip install py2exe
echo Finished.
