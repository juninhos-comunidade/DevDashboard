from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth_schema import (LoginRequest,TokenResponse)
from app.core.auth_dependency import get_current_user
from app.database.criar_database import get_db
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
    
@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest,db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        return service.authenticate_user(
            data.email,
            data.password
        )
    except ValueError as v:
        raise HTTPException(status_code=401, detail=str(v))
    
@router.get("/me")    
def user_me(current=Depends(get_current_user), db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user_by_id(int(current))

    return {
        "id":user.id,
        "name": user.name,
        "email":user.email
    }          