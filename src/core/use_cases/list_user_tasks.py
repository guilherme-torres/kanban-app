from typing import List
from src.core.repository_interfaces.user_repository import IUserRepository
from src.core.repository_interfaces.task_repository import ITaskRepository
from src.core.entities.task import Task
from src.core.use_cases.exceptions import UserNotFoundError


class ListUserTasksUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
        task_repository: ITaskRepository,
    ):
        self.user_repository = user_repository
        self.task_repository = task_repository

    def execute(self, user_id: int) -> List[Task]:
        user_exist = self.user_repository.find_by_id(user_id)
        if not user_exist:
            raise UserNotFoundError("User not found")
        return self.task_repository.filter_by({"user_id": user_id})
