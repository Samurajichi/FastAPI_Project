from fastapi import APIRouter, status
from uuid import UUID

from database.core import DbSession
from . import models
from . import service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_users( db: DbSession):
    print("get method is evaluated")
    return service.get_users(db)