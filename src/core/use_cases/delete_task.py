from src.core.repository_interfaces.task_repository import ITaskRepository
from src.core.use_cases.exceptions import TaskNotFoundError


class DeleteTaskUseCase:
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    def execute(self, task_id: int) -> None:
        task_exist = self.task_repository.find_by_id(task_id)
        if not task_exist:
            raise TaskNotFoundError("Task not found")
        return self.task_repository.delete(task_id)
