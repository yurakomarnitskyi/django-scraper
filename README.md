# Django Scraper Project

This project is designed for scraping an automotive website and storing the data in a Django database.

## Installation

### System Requirements

Make sure the following components are installed on your system:

- Docker
- Docker Compose

### Installation Instructions

1. Clone the repository: `https://github.com/yurakomarnitskyi/django-scraper.git`
2. Navigate to the project directory: `cd django-scraper`
3. Start Docker Compose: `docker-compose up`
4. Dump the db now by running this command in a new console: `docker-compose exec app python app/db_dump.py`
5. See this db data by opening this directory: `docker exec -it <container_name_or_id> /bin/bash`, `cd usr/src/django-scraper/dumps`, `cat filename.json`
 or use DockerDesktop

### Managing Daemons
To control daemons within the Snort container, open another bash window:

`docker exec -it snort bash`

Use the following commands to manage processes::

1. `supervisorctl status`
2. `supervisorctl status process_name`3
3. `supervisorctl restart process_name`
4. `supervisorctl stop process_name`
5. `supervisorctl start process_name`

### Notice, that we have 1 processes:`

- cron - runs cron with script for auto clearing table with events in database weekly (12:00 every day)
   

## Usage

The project utilizes Django, PostgreSQL, BeautifulSoup for scraping, and Docker for containerization.


