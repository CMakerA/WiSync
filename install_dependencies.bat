@echo off
if not exist "C:\Python34\python.exe" if not exist "C:\Users\Arnym\AppData\Local\Programs\Python\Python36-32\python.exe" (
    goto installpython
)
echo Python already installed.
goto installpygame

:installpython
echo Installing Python 3.6.4

SET downloadUrl=https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe
SET tempFile=%cd%\.%random%-tmp

echo "Downloading..."

BITSADMIN /transfer /download %downloadUrl% %tempFile% >nul

echo "ok"

start %tempFile%
del %tempFile%
goto installpygame

:installpygame
echo Installing pygame
python -m pip install pygame > null && (
    goto installpy2exe
) || (
if exist "C:\Python34\python.exe" (
    C:\Python34\python.exe -m pip install pygame
    goto installpy2exe
)
if exist "C:\Python34\python.exe" (
    C:\Users\Arnym\AppData\Local\Programs\Python\Python36-32\python.exe -m pip install pygame
    goto installpy2exe
)
)

:installpy2exe
echo Installing py2exe
python -m pip install py2exe > null && (
    goto end
) || (
if exist "C:\Python34\python.exe" (
    C:\Python34\python.exe -m pip install py2exe
    goto end
)
if exist "C:\Python34\python.exe" (
    C:\Users\Arnym\AppData\Local\Programs\Python\Python36-32\python.exe -m pip install py2exe
    goto end
)
)

:end
echo Finished.
PAUSE