
## Backend environment preparation (Windows)

1. install Python
2. Install PIP package manager
3. Go to the main project directory (where the current readme.md file is located) and execute:

```
python -m pip install virtualenv
python -m venv venv
venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata jachty_api/fixtures/initial_data.json
```

## Backend RUN (Windows)

1. Go to the main project directory (where the current readme.md file is located) and execute:

```
venv\Scripts\activate.bat
python manage.py runserver 8888
```