from typing import List
from src.core.use_cases.create_task import CreateTaskUseCase
from src.core.use_cases.list_user_tasks import ListUserTasksUseCase
from src.core.use_cases.update_task import UpdateTaskUseCase
from src.core.use_cases.delete_task import DeleteTaskUseCase
from src.adapters.schemas.task import TaskCreate, TaskResponse
from src.core.entities.task import Task


class TaskController:
    def __init__(
        self,
        create_task_use_case: CreateTaskUseCase,
        list_user_tasks_use_case: ListUserTasksUseCase,
        update_task_use_case: UpdateTaskUseCase,
        delete_task_use_case: DeleteTaskUseCase,
    ):
        self.create_task_use_case = create_task_use_case
        self.list_user_tasks_use_case = list_user_tasks_use_case
        self.update_task_use_case = update_task_use_case
        self.delete_task_use_case = delete_task_use_case

    def create_task(self, task_data: TaskCreate) -> TaskResponse:
        task = Task(
            title=task_data.title,
            description=task_data.description,
            start=task_data.start,
            end=task_data.end,
            user_id=task_data.user_id,
            status_id=task_data.status_id,
        )
        created_task = self.create_task_use_case.execute(task)
        return TaskResponse(
            id=created_task.id,
            title=created_task.title,
            description=created_task.description,
            start=created_task.start,
            end=created_task.end,
            user_id=created_task.user_id,
            status_id=created_task.status_id,
        )

    def list_user_tasks(self, user_id: int) -> List[TaskResponse]:
        tasks = self.list_user_tasks_use_case.execute(user_id)
        return list(
            map(
                lambda task: TaskResponse(
                    id=task.id,
                    title=task.title,
                    description=task.description,
                    start=task.start,
                    end=task.end,
                    user_id=task.user_id,
                    status_id=task.status_id,
                ),
                tasks,
            )
        )

    def update_task(self, task_id: int, task_data: TaskCreate) -> TaskResponse:
        updated_task = self.update_task_use_case.execute(
            task_id=task_id, task_data=task_data.model_dump(exclude_unset=True)
        )
        return TaskResponse(
            id=updated_task.id,
            title=updated_task.title,
            description=updated_task.description,
            start=updated_task.start,
            end=updated_task.end,
            user_id=updated_task.user_id,
            status_id=updated_task.status_id,
        )

    def delete_task(self, task_id: int) -> None:
        return self.delete_task_use_case.execute(task_id)
