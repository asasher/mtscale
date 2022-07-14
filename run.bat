@ECHO OFF
set /p refresh="Enter the refresh frequency in seconds: "
CALL %~dp0\env\Scripts\activate
python %~dp0\mtscale.py --refresh %refresh%
PAUSE
