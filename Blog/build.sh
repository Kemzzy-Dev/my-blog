#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py createsuperuser --no-input --username admin --email kemzzy17@gmail.com 
python manage.py migrate
