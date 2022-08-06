#!/bin/bash

export MYSQL_PWD=${DB_PASSWORD}
mysql -h ${DB_HOST} -u ${DB_USER} -e "drop database ${DB_NAME};"
mysql -h ${DB_HOST} -u ${DB_USER} -e "create database ${DB_NAME};"

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

echo "----- register_person -----"
python3 manage.py register_person
