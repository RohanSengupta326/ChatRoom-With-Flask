# Introduction

This is a chat application, implemented using Flask-SocketIO with both the database (PostgreSQL) and the app deployed in Heroku. It also has user registration and authentication functionalities.

## Demo

RChat - Chat rooms are back in style!

## Files in the program

    - **application.py** : This is the main app file and contains both the registration/login page logic and the Flask-SocketIO backend for the app.

    - **models.py** : Contains Flask-SQLAlchemy models used for user registration and login in application.py

    - **wtform_fields.py** : Contains the classes for WTForms/Flask-WTF and the custom validators for the fields

    - **create.py** : optional file only required if repo is to be cloned. See 'Usage' section below.
    
    - **Procfile** : file required for Heroku
    requirements.txt: list of Python packages installed (also required for Heroku)
    
    - **templates/** : folder with all HTML files
    
    - **static/** : for with all JS scripts and CSS files


## Run app - 
**Link** - [http://rchat-app.herokuapp.com/](http://rchat-app.herokuapp.com/)


## Clone/Modify app

    1. Modify application.py to replace the secret key (i.e. os.environ.get('SECRET')) with a secret key of your choice and the database link (i.e. os.environ.get('DATABASE_URL')) with the link to your own database.

    The two lines to be edited in application.py are shown below:

    ```
    app.secret_key=os.environ.get('SECRET')
    app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
    ```

    2. Edit create.py to once again replace os.environ.get('DATABASE_URL') with the link to your database.

    3. Run create.py from the terminal to create the table to hold user credentials.

    ```
    foo@bar:~$ python create.py
    ```