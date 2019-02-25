# DRF
A basic employee-api with django rest framework.
# First Steps
Before starting the web api based on django rest framework its necessary install all dependencies as we always do when start developing django projects. Good practices says that we have to setup a new python environment for each time we start a django project.
```
virtualenv virtual
```
virtual is the name of the pythons virtual environment. After that we have to activate this virtual environment by doing:
```
source virtual/bin/activate
```
**Django and Django Rest Framework installations**
```
pip install django
```
```
pip install djangorestframework
```
**Starting the project and the app**
```
django-admin startproject myproject
```
```
django-admi startapp myapp
```
Now the django project (myproject) and our application (myapp) are created. Next we will create the superuser and then do the migration for the first time.
```
cd myproject
```
```
python manage.py createsuperuser
```
```
Username (leave blank to use 'computer-user'): 
Email address: 
Password:
```
```
python manage.py migrate
```
# The API
**Setting.py**
