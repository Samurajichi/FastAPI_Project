from sqlalchemy import create_engine
from dotenv import load_dotenv
from fastapi import Depends
import os
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from typing import Annotated, Union
from sqlmodel import SQLModel,Field

load_dotenv()

database_url = os.getenv('DATABASE_URL')

engine = create_engine(str(database_url))
print("DATABASE_URL:", database_url, type(database_url))  # Debugowanie
print("Environment variables:", os.environ)  # Debugowanie
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Hero(SQLModel, table=True):
    id: Union[int, None] = Field(default=None, primary_key=True)
    name: str
    superpower: str


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        create_db_and_tables()
        yield db
    finally:
        db.close()

DbSession = Annotated[Session, Depends(get_db)]

