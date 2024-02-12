import os
from datetime import datetime
from django.core.management import call_command
from django import setup
import logging

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
setup()  

logger = logging.getLogger('scraper')

DB_NAME = os.getenv("DB_NAME")

def dump_database():
    dump_dir = "dumps/"
    os.makedirs(dump_dir, exist_ok=True)
    
    dump_path = f"{dump_dir}db_dump_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    
    with open(dump_path, 'w') as dump_file:
        call_command('dumpdata', '--exclude', 'contenttypes', '--exclude', 'auth.permission', '--format=json', stdout=dump_file)
    
    print(f"Database dumped to {dump_path}")
    
    logger.info(f"Database dumped to {dump_path}")

if __name__ == "__main__":
    dump_database()
