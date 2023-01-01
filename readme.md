
# Windows preparation

## Backend environment preparation and test database creation (Windows)

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

## RUN Backend (Windows)

1. Go to the main project directory (where the current readme.md file is located) and execute:

```
venv\Scripts\activate.bat
python manage.py runserver 8888
```

## Frontend environment preparation (Windows)

1. Install NPM package manager
2. Install Vue.js

```
npm install -g @vue/cli
npm audit fix --force
npm install --location=global yarn
yarn add vue-router@4
```

## RUN Frontend (Windows)

1. Go to jachty_application/ directory

```
yarn serve
```

# Ubuntu preparation

## Backend environment preparation and test database creation
```
sudo apt-get update
pip3 install virtualenv
virtualenv venv2
. venv2/bin/activate
pip3 install -r requirements.txt
python3 manage.py createsuperuser
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata jachty_api/fixtures/initial_data.json
```

## RUN Backend
```
python3 manage.py runserver 8888
```

## Frontend environment preparation
```
sudo apt-get update
sudo apt install nodejs npm
```