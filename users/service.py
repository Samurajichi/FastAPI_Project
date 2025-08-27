from . import models
from sqlalchemy.orm import Session
from entities.user import User
import logging
from errorHandling.errors import UserNotFoundError 



def get_users(db: Session) -> models.UserResponse:
    user = db.query(User).first()
    # if not user:
    #     logging.warning(f"User not found.")
    #     raise UserNotFoundError()
    logging.info(f"Successfully retrieved user")
    return user