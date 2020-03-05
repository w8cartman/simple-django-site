#!/bin/bash

#Migrate
python manage.py makemigrations
python manage.py migrate

#Start server
python manage.py runserver 0.0.0.0:8000
