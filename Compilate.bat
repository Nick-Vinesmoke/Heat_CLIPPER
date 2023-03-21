@echo off
pip install pyinstaller
pip install pyperclip
pip install pywin32


pyinstaller -F -w -i icon.ico --add-data "data.py;." HeatClipper.py.py



rmdir /s /q build
:cmd
pause null