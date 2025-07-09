from abc import ABC, abstractmethod
from typing import List, Union
from src.core.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Union[User, None]:
        pass

    @abstractmethod
    def list_all(self) -> List[User]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Union[User, None]:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
