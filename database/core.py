from sqlalchemy import create_engine
from dotenv import load_dotenv
from fastapi import Depends
import os
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from typing import Annotated
from sqlmodel import SQLModel,Field

load_dotenv()

database_url = os.getenv('DATABASE_URL')

engine = create_engine(str(database_url))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DbSession = Annotated[Session, Depends(get_db)]

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    superpower: str


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)