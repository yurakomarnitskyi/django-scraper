FROM python:latest

WORKDIR /root/django_scraper/


RUN apt-get update && apt-get install -y cron supervisor

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app ./app

COPY configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY configs/cronfile /etc/cron.d/cronfile

RUN crontab /etc/cron.d/cronfile

ENTRYPOINT /usr/bin/supervisord
