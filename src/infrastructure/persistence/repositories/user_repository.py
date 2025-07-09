from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.core.repository_interfaces.user_repository import IUserRepository
from src.core.entities.user import User
from src.infrastructure.persistence.models.user import User as UserModel


class UserRepository(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, user: User) -> User:
        user_db = UserModel(
            name=user.name,
            email=user.email,
            password=user.password
        )
        self.session.add(user_db)
        self.session.commit()
        self.session.refresh(user_db)
        return User(
            id=user_db.id,
            name=user_db.name,
            email=user_db.email,
            password=user_db.password
        )

    def find_by_id(self, id: int) -> Optional[User]:
        user_db = self.session.get(UserModel, id)
        return User(
            id=user_db.id,
            name=user_db.name,
            email=user_db.email,
            password=user_db.password
        ) if user_db else None

    def list_all(self) -> List[User]:
        users_db = self.session.scalars(select(UserModel)).all()
        return list(map(lambda user: User(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password
        ), users_db))

    def find_by_email(self, email: str) -> Optional[User]:
        user_db = self.session.scalars(select(UserModel).filter_by(email=email)).first()
        return User(
            id=user_db.id,
            name=user_db.name,
            email=user_db.email,
            password=user_db.password
        ) if user_db else None

    def delete(self, id: int) -> None:
        user_db = self.session.get(UserModel, id)
        self.session.delete(user_db)
        self.session.commit()
