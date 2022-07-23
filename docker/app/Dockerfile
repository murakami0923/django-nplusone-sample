# FROM ubuntu:20.04
FROM python:3.9.9

ARG ENV=develop

# アプリケーション実行用ユーザーを作成
RUN addgroup --gid 60000 app_user
RUN adduser --gid 60000 --uid 60000 app_user

RUN ls -la /home/app_user/

# # apt update, upgrade
RUN apt update
# RUN apt upgrade -y

# # Pythonインストール用リポジトリを追加
# RUN apt install -y software-properties-common
# RUN add-apt-repository ppa:deadsnakes/ppa

# RUN apt update

# # Python任意のバージョンインストール（ここでは3.9）
# RUN apt install -y python3.9 python3.9-venv python3.9-dev
# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 10
# RUN update-alternatives --set python /usr/bin/python3.9

# Python確認
RUN which python
RUN python -V
RUN ls -l /usr/bin/

# venv
USER app_user
RUN mkdir -p ~/venv/python3.9
RUN cd ~/venv/python3.9/ \
    && python -m venv django-docker-sample \
    && ls -la django-docker-sample/bin/
USER root

# mysqlクライアント
# RUN apt install -y gcc libmariadb-dev
# RUN apt install -y mysql-client
RUN apt install -y default-mysql-client
# pipでmysqlclientを使うときに必要
RUN apt install -y build-essential
RUN apt install -y libmariadb-dev

# MySQLクライアント確認
RUN which mysql
RUN mysql --version

COPY db-app-user-password.sh /root/db-app-user-password.sh
RUN chmod a+x /root/db-app-user-password.sh

# # pip
# RUN apt install -y python3-pip
# RUN gcc --version
# RUN python -m pip install pip \
#     && pip install --upgrade pip

# USER app_user
# RUN "/bin/bash" "-c" "python -m pip install pip; pip install --upgrade pip"
# USER root

# uWSGIのログ、プロセス用のディレクトリ作成、所有者変更
RUN cd /var/log/ \
&& mkdir uwsgi \
&& chown app_user:app_user uwsgi \
&& cd /var/run/ \
&& mkdir uwsgi \
&& chown app_user:app_user uwsgi

# /var/run/uwsgiを自動的に作るよう設定
RUN mkdir -p /etc/tmpfiles.d/
RUN cd /etc/tmpfiles.d/ \
&& echo "d /var/run/uwsgi 0755 app_user app_user" >> uwsgi.conf

# uWSGI Emperor mode設置
# RUN mkdir -p /etc/uwsgi/vassals \
# && ln -s /home/app_user/app/app_uwsgi.ini /etc/uwsgi/vassals/
COPY uwsgi/app_uwsgi.ini /etc/uwsgi/vassals/

# uWSGI起動環境変数の定義ファイルを設置
# 【注意】本番と開発で別ファイルで定義しているので、コピー元のファイルを間違えないように！
COPY ${ENV}/django_app_module /etc/sysconfig/

# # uWSGIサービス起動スクリプト設置
# COPY uwsgi/uwsgi.service /etc/systemd/system/

# # uWSGIの自動起動設定
# RUN systemctl enable uwsgi

# アプリケーションインストールスクリプト
COPY ${ENV}/app-install.sh /home/app_user/
RUN chown app_user:app_user /home/app_user/app-install.sh

# アプリケーション
COPY app.tar.gz /home/app_user/app.tar.gz

RUN cd /home/app_user/ \
    chown app_user:app_user app.tar.gz

USER app_user

RUN cd ~/ \
    && tar zxf app.tar.gz

RUN ls -l ~/venv/python3.9/django-docker-sample/bin/

RUN cd ~/app/ \
    && /bin/bash ~/app-install.sh

USER root

RUN apt upgrade -y

ENTRYPOINT [ "/sbin/init" ]