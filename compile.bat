@echo off
title WiSync Compiler

echo Press any key for start compiling...
PAUSE > null

call install_dependencies_compiler.bat

c:\Python34\python.exe setup.py install

c:\Python34\python.exe setup.py py2exe

echo Compilation finished, press any key to exit.
PAUSE > null