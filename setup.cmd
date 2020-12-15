start "" "http://www.google.com"
start cmd /k git status
start cmd /k psql -U postgres
start cmd /c code .
CALL env\Scripts\activate.bat
set FLASK_APP=manage.py
set FLASK_DEBUG=1
cmd /k