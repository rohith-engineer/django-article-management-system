#!/bin/sh
set -e

echo "ENV_STATE = $ENV_STATE"

if [ "${ENV_STATE^^}" = "PRODUCTION" ]; then

    echo "Starting Django in PRODUCTION"
    export DJANGO_SETTINGS_MODULE=djangocourse.settings
    python manage.py migrate
    python manage.py collectstatic --noinput
    gunicorn djangocourse.wsgi:application --bind 0.0.0.0:8000
else
    echo "Starting Django in DEVELOPMENT"
    export DJANGO_SETTINGS_MODULE=djangocourse.settings
    python manage.py runserver 0.0.0.0:8000
fi

