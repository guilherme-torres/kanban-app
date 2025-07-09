from typing import Dict, Any
from src.core.repository_interfaces.task_repository import ITaskRepository
from src.core.repository_interfaces.status_repository import IStatusRepository
from src.core.entities.task import Task
from src.core.use_cases.exceptions import TaskNotFoundError, StatusNotFoundError


class UpdateTaskUseCase:
    def __init__(
        self,
        task_repository: ITaskRepository,
        status_repository: IStatusRepository,
    ):
        self.task_repository = task_repository
        self.status_repository = status_repository

    def execute(self, task_id: int, task_data: Dict[str, Any]) -> Task:
        task_exist = self.task_repository.find_by_id(task_id)
        if not task_exist:
            raise TaskNotFoundError("Task not found")
        if 'status_id' in task_data.keys():
            status_exist = self.status_repository.find_by_id(task_data.get('status_id'))
            if not status_exist:
                raise StatusNotFoundError("Status not found")
        return self.task_repository.update(task_id, task_data)
