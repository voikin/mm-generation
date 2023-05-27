import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get('DB_USER', 'root')
DB_PASS = os.environ.get('DB_PASS', 'root')
DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'mm')

mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017')