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

cd /tmp/dump/
MYSQL_PWD=${DB_PASSWORD}
mysql -h ${DB_HOST} -u ${DB_USER} ${DB_NAME} < ${DB_NAME}.dmp

cd /usr/local/app/
python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8001