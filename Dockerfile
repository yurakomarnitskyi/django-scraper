FROM python:latest
RUN apt-get update && apt-get install -y supervisor && apt-get install cron -y

COPY . /usr/src/django-scraper

WORKDIR /usr/src/django-scraper

ADD crontab /etc/cron.d/my-cron-file
RUN echo "" >> /etc/cron.d/my-cron-file

COPY requirements.txt ./
RUN pip install -r requirements.txt


