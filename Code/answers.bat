@echo off

REM Define the server address and port
set SERVER=chals.swampctf.com
set PORT=60001

REM Send each number to the server using Netcat

echo 203 | nc %SERVER% %PORT%
pause

echo 1256 | nc %SERVER% %PORT%
pause

echo 1218 | nc %SERVER% %PORT%
pause

echo 1967 | nc %SERVER% %PORT%
pause
echo Sending: 4644
echo 4644 | nc %SERVER% %PORT%
pause
