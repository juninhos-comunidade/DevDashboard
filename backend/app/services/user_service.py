from sqlalchemy.orm import Session

from app.models.user_models import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password


class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(
        self,
        db: Session,
        user_data: UserCreate
    ):
        existing_user = self.repository.find_by_email(
            db,
            user_data.email
        )

        if existing_user:
            raise ValueError(
                "Email já cadastrado"
            )

        user = User(
            name=user_data.name,
            email=user_data.email,
            password_hash=hash_password(
                user_data.password
            )
        )

        return self.repository.create(
            db,
            user
        )