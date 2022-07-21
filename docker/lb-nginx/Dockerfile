FROM ubuntu:20.04

ARG ENV=develop

RUN apt update
RUN apt upgrade -y

RUN apt install -y systemctl
RUN apt install -y init
RUN apt install -y systemd
RUN apt install -y nginx

RUN apt install -y openssl

RUN mkdir /root/install/
COPY localhost-cert.tar.gz /root/install/

RUN mkdir -p /etc/nginx/ssl/
RUN chmod 700 /etc/nginx/ssl/

RUN cd /root/install/ \
    && tar zxf localhost-cert.tar.gz \
    && mv localhost-cert/* /etc/nginx/ssl/

# COPY localhost.conf /etc/nginx/sites-available/
COPY localhost.conf /etc/nginx/conf.d/

RUN systemctl enable nginx

ENTRYPOINT [ "/sbin/init" ]