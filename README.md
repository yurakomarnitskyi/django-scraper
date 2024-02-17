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


### Notice, that we have 1 processes:`
- Scarp data (12:00 every day)
- And dump db every-day (17:00)
   

## Usage
The project utilizes Django, PostgreSQL, BeautifulSoup, Celery, Docker.


