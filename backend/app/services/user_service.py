from sqlalchemy.orm import Session

from app.models.user_models import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password
from app.core.security import verify_password
from app.core.jwt import create_access_token


class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(
        self,
        user_data: UserCreate
    ):
        existing_user = self.repository.find_by_email(
            user_data.email
        )

        if existing_user:
            raise ValueError(
                "Email já cadastrado"
            )

        print("PASSWORD:", user_data.password)
        print("LEN:", len(user_data.password))
        password_hashc = hash_password(user_data.password)

        return self.repository.create_user(
            name=user_data.name,
            email=user_data.email,
            password_hash=password_hashc
        )
    
    def authenticate_user(self,email: str,password: str):
        user = self.repository.find_by_email(email)

        if not user:
            raise ValueError(
                "Credenciais inválidas"
            )

        if not verify_password(
            password,
            user.password_hash
        ):
            raise ValueError(
                "Credenciais inválidas"
            )

        token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }