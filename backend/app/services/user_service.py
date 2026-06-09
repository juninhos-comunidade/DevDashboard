from app.models.user_models import User
from app.repositories.user_repository import UserRepository
from app.database.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


class UserService:
    def __init__(self):
        load_dotenv()
        DATABASE_URL = os.getenv("DATABASE_URL")
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.session = SessionLocal()
        self.user_repository = UserRepository(self.session)

    def create_user(self, name: str, email: str, password_hash: str) -> User:
        return self.user_repository.create_user(name, email, password_hash)

    def get_user_by_email(self, email: str) -> User | None:
        return self.user_repository.get_user_by_email(email)
    
    def get_user_by_id(self, user_id: int) -> User | None:
        return self.user_repository.get_user_by_id(user_id)