@echo off
if not exist "C:\Python34\python.exe" goto installpython
echo Python already installed.
goto installpygame

:installpython
echo Installing Python3.4.3

SET downloadUrl=https://www.python.org/ftp/python/3.4.3/python-3.4.3.msi
SET tempFile=%cd%\.%random%-tmp

BITSADMIN /transfer /download %downloadUrl% %tempFile% >nul

start %tempFile%
del %tempFile%
goto installpygame

:installpygame
echo Installing pygame
C:\Python34\python.exe -m pip install pygame > null
goto installpy2exe

:installpy2exe
echo Installing py2exe
C:\Python34\python.exe -m pip install py2exe > null
goto end

:end
echo Finished.