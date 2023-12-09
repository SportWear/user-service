import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME', 'postgres')
DB_USER = os.getenv('DB_USER', 'admin')
DB_PASS = os.getenv('DB_PASS', 'admin')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_HOST = os.getenv('DB_HOST', 'localhost')
