from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/fastapi"

# Engine responsible for establishing connection to DB.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Get a session to database for every request to our API
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()