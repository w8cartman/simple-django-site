#!/bin/bash

#Migrate
python manage.py makemigrations
python manage.py migrate

#Run tests
python3 manage.py test mainApp || echo "test failed" > failed.err
