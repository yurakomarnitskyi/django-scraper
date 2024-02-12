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
3. Start Docker Compose: `docker-compose up -d`
4. Dump the db now by running this command in a new console: `docker-compose exec app python app/db_dump.py`
5. See this db data by opening this directory: `usr/src/django-scraper/dump`


## Usage

The project utilizes Django, PostgreSQL, BeautifulSoup for scraping, and Docker for containerization.


