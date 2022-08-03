@ECHO OFF
set /p outfile="Enter the name of the output file: "
set /p refresh="Enter the refresh frequency in seconds: "
set /p port="Enter the port the device is connected to: "
CALL %~dp0\env\Scripts\activate
python %~dp0\mtscale.py --out %outfile% --refresh %refresh% --port %port%
PAUSE
