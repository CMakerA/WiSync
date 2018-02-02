@ECHO OFF
REM usage: append_system_path "path"
SET Key="HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
IF EXIST C:\Python34\python.exe (
    FOR /F "usebackq tokens=2*" %%A IN (`REG QUERY %Key% /v PATH`) DO Set CurrPath=C:\Python34
    goto installpygame
)
IF EXIST C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python36-32\python.exe (
    FOR /F "usebackq tokens=2*" %%A IN (`REG QUERY %Key% /v PATH`) DO Set CurrPath=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python36-32
    goto installpygame
)
ECHO %CurrPath% > system_path_bak.txt
SETX PATH "%CurrPath%";%1 /M