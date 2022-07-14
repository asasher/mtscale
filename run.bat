@ECHO OFF
set /p outfile="Enter the name of the output file: "
set /p refresh="Enter the refresh frequency in seconds: "
CALL %~dp0\env\Scripts\activate
python %~dp0\mtscale.py --out %outfile% --refresh %refresh%
PAUSE
