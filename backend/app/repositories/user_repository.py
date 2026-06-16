from sqlalchemy.orm import Session
from app.models.user_models import User
from app.database.base import Base






class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, name: str, email: str, password_hash: str) -> User:
        new_user = User(name=name, email=email, password_hash=password_hash)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def find_by_email(self, email: str) -> User | None:
        return self.session.query(User).filter(User.email == email).first()
    
    def get_user_by_id(self, user_id: int) -> User | None:
        return self.session.query(User).filter(User.id == user_id).first()
    
    