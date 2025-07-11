from typing import List
from src.core.repository_interfaces.user_repository import IUserRepository
from src.core.repository_interfaces.status_repository import IStatusRepository
from src.core.entities.status import Status
from src.core.use_cases.exceptions import UserNotFoundError, ApplicationError


class ListUserStatusUseCase:
    def __init__(
        self,
        status_repository: IStatusRepository,
        user_repository: IUserRepository,
    ):
        self.user_repository = user_repository
        self.status_repository = status_repository

    def execute(self, user_id: int) -> List[Status]:
        if not user_id:
            raise ApplicationError("user_id required")
        user_exist = self.user_repository.find_by_id(user_id)
        if not user_exist:
            raise UserNotFoundError("User not found")
        return self.status_repository.filter_by({"user_id": user_id})
