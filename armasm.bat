@echo off

if [%2] NEQ [o] goto usage
python myassembler.py %*
goto :eof
:usage
@echo Usage: %0 ^<Not recognized as a command^>
exit /B 1

pause