@echo off
echo Installing Self-Hosted Trello...

echo Creating virtual environment...
python -m venv env

echo Activating virtual environment...
call env\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Initializing database...
python -m self_hosted_trello.database

echo Starting server...
python -m self_hosted_trello.server

echo Installation complete. You can now access the application at http://localhost:5000
pause