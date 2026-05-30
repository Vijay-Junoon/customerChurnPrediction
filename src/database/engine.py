from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

database_url = (
  f"postgresql://{DB_USER}:"
  f"{DB_PASSWORD}@"
  f"{DB_HOST}:{DB_PORT}/"
  f"{DB_NAME}"
)

engine = create_engine(database_url)