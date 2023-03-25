# Django Marketplace
This is a django app created following youtube guide: https://www.youtube.com/watch?v=ZxMB6Njs3ck&list=WL

## endpoints
TBD

## helpers
```bash
python3 -m venv env
source env/bin/activate
pip install django
python -m pip install Pillow
django-admin startproject puddle #create project
cd puddle
python manage.py runserver #run server
python manage.py startapp core #create a new django app
python manage.py startapp item #create a new django app
```

## manage migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## users
```bash
# to be able to manage authentication the admin user needed
python manage.py create superuser
```

44:25