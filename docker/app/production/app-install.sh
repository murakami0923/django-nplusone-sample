#!/bin/bash
cd ~/app
source ~/venv/python3.9/django-docker-sample/bin/activate
which python
python -V
pip install --upgrade pip
cd ~/app/requirements/
pip install -r production.txt
pip freeze > ~/pip-freeze.txt

cd ~/app/
DJANGO_SECRET_KEY=GT3MT5b9q2Vs2kMvtVFaLeiDNn7Fwyim
DJANGO_ADMIN_URL=admin
DJANGO_STTINGS_MODULE=config.settings.develop
python manage.py collectstatic
