start "" "http://localhost:5000"
start cmd /k git status
start cmd /k psql -U postgres
CALL code .
CALL env\Scripts\activate.bat
set FLASK_APP=manage.py
set FLASK_DEBUG=1
CALL flask run
cmd /k