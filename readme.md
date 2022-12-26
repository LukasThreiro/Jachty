
## Przygotowanie backend
```
python -m venv venv
venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata jachty_api/fixtures/initial_data.json
```

## Uruchamianie backend

`python manage.py runserver 8888`