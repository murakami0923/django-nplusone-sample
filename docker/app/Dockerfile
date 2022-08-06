# FROM ubuntu:20.04
FROM python:3.9.9

ARG ENV
ARG ENV_APP_GID
ARG ENV_APP_GNAME
ARG ENV_APP_UID
ARG ENV_APP_UNAME

# アプリケーション実行用ユーザーを作成
RUN addgroup --gid ${ENV_APP_GID} ${ENV_APP_GNAME}
RUN adduser --gid ${ENV_APP_GID} --uid ${ENV_APP_UID} ${ENV_APP_UNAME}

RUN ls -la /home/${ENV_APP_UNAME}/

RUN apt update

# Python確認
RUN which python
RUN python -V
# RUN ls -l /usr/bin/

# mysqlクライアント
RUN apt install -y default-mysql-client
# pipでmysqlclientを使うときに必要
RUN apt install -y build-essential
RUN apt install -y libmariadb-dev

# MySQLクライアント確認
RUN which mysql
RUN mysql --version

# アプリケーションディレクトリ
RUN mkdir -p /usr/local/app/
RUN chown ${ENV_APP_UNAME}:${ENV_APP_GNAME} /usr/local/app/

# アプリケーション用pip
COPY requirements /tmp/requirements

WORKDIR /tmp/requirements/

RUN pip install --upgrade pip

RUN pip install -r production.txt
RUN pip install -r local.txt

RUN apt upgrade -y

# entrypointのsh
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod a+x /usr/local/bin/entrypoint.sh

# init-dbのsh
COPY init-db.sh /usr/local/bin/init-db.sh
RUN chmod a+x /usr/local/bin/init-db.sh

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]