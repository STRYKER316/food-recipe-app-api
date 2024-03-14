#!/bin/sh

set -e

python manage.py wait_fo_db
python mannage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
