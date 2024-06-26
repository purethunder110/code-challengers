from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker,scoped_session
import os
from dotenv.main import load_dotenv

load_dotenv()

url=URL.create(
    drivername=os.getenv("DB_DRIVER"),
    username=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT"),
)

engine=create_engine(url,pool_size=int(os.getenv("POOL_SIZE")),max_overflow=int(os.getenv("MAX_OVERFLOW")))

conn=engine.connect()

session_factory=sessionmaker(bind=engine)
session_threaded=scoped_session(session_factory)