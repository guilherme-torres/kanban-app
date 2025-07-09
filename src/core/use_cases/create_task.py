from src.core.repository_interfaces.task_repository import ITaskRepository
from src.core.repository_interfaces.user_repository import IUserRepository
from src.core.repository_interfaces.status_repository import IStatusRepository
from src.core.entities.task import Task
from src.core.use_cases.exceptions import UserNotFoundError, StatusNotFoundError


class CreateTaskUseCase:
    def __init__(
        self,
        task_repository: ITaskRepository,
        user_repository: IUserRepository,
        status_repository: IStatusRepository,
    ):
        self.task_repository = task_repository
        self.user_repository = user_repository
        self.status_repository = status_repository

    def execute(self, task: Task) -> Task:
        user_exist = self.user_repository.find_by_id(task.user_id)
        if not user_exist:
            raise UserNotFoundError("User not found")
        status_exist = self.status_repository.find_by_id(task.status_id)
        if not status_exist:
            raise StatusNotFoundError("Status not found")
        return self.task_repository.save(task)
