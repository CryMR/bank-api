from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL: postgresql://user:password@postgresserver/db_name
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:karamatsu@db:5432/bankdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()