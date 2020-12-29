# Chatty App

This is a basic flask website in which I have developed basic user authentication system.

## Technologies Used

* Flask and other useful libraries
* HTML
* CSS
* Bootstrap

## Steps to start the server

1. Open the root directory in your terminal.
2. Set MAIL_USERNAME and MAIL_PASSWORD environment variables. Set MAIL_USERNAME to your email. Set MAIL_PASSWORD to app password if you are using gmail.
3. Make a Python envronment in the root directory and activate it.
4. Install all the libraries mentioned in 'requirements.txt' file.
5. Set SQLALCHEMY_DATABASE_URI to your preferred database.
6. Set SECRET_KEY environment variable.
7. Type "flask db init" in your terminal
8. Type 'flask db migrate -m "Databse migration"'.
9. Type 'flask db upgrade'.
10. Set FLASK_APP = manage.py
11. Set FLASK_DEBUG = 1
12. Type 'flask run'
13. Open your browser and type 'localhost:5000' in search bar
14. You are ready to go!