#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python ./Blog/manage.py collectstatic --no-input
python ./Blog/manage.py migrate
