#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py createsuperuser --no-input --username admin --pasword 2fK9f@example.com 
python manage.py migrate
