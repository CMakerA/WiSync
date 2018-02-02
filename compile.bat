@echo off
title WiSync Compiler

echo Press any key for start compiling...
PAUSE > null

IF exist dist (
rd /s /q dist
)

call install_dependencies_compiler.bat

python setup.py install

python setup.py py2exe

echo Compilation finished, press any key to exit.
PAUSE > null