#!/bin/bash

python manage.py migrate

export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_EMAIL="admin@manchild.dev"
export DJANGO_SUPERUSER_PASSWORD="s@mplePas$$w0rd"

python manage.py createsuperuser --noinput

python manage.py runserver 0.0.0.0:8000
