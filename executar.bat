@echo off
cd /d %~dp0

echo Instalando dependencias...
C:\Users\arthu\AppData\Local\Python\pythoncore-3.14-64\python.exe -m pip install -r requirements.txt

echo Rodando o programa...
C:\Users\arthu\AppData\Local\Python\pythoncore-3.14-64\python.exe programa.py

pause