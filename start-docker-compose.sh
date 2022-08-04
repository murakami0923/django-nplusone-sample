#!/bin/sh

# mariadb ログ用ディレクトリのパーミッションを777に
VOL_LOG_PATH="./volumes/mysql/log/"

if [ ! -d ${VOL_LOG_PATH} ]; then
    sudo mkdir -p ${VOL_LOG_PATH}
fi

sudo chmod 777 ${VOL_LOG_PATH}

docker compose up -d
