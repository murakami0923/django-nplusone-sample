#!/bin/bash

# MySQLの起動を待つ
host=${DB_HOST}
user=${DB_USER}
export MYSQL_PWD=${DB_PASSWORD}

echo "Waiting for mysql"
while ! mysqladmin ping -h ${host} --silent; do echo -n "."; sleep 1; done

echo " "
echo "mysql connect ok."

pwd=`pwd`

cd /usr/local/app/

ls -lrth

echo "----- makemigrations -----"
python3 manage.py makemigrations
echo "----- migrate -----"
python3 manage.py migrate

echo "----- truncate_all_data -----"
python3 manage.py truncate_all_data
echo "----- register_sex -----"
python3 manage.py register_sex
echo "----- register_district_prefecture -----"
python3 manage.py register_district_prefecture

echo "----- collectstatic -----"
python3 manage.py collectstatic --noinput

echo "----- runserver 0.0.0.0:8001 -----"
python3 manage.py runserver 0.0.0.0:8001

echo "----- register_person -----"
python3 manage.py register_person

