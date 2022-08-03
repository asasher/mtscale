@ECHO OFF
python -m venv env
pip install -r %~dp0\requirements.txt
PAUSE
