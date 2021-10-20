import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()

# SQL DB configuration
HOST = os.environ.get('POSTGRES_HOST')
USER = os.environ.get('POSTGRES_USER')
PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DATABASE = os.environ.get('POSTGRES_DB')
SCHEMA = os.environ.get('POSTGRES_SCHEMA')

WEATHER_URL=os.environ.get('WEATHER_URL')