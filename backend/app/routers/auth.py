from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user_schema import (
    UserCreate,
    UserResponse
)
from app.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register", response_model=UserResponse)
    
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        service = UserService(db)

        return service.create_user(user)

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )