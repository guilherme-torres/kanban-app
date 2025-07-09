from typing import List, Optional, Dict, Any
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.core.repository_interfaces.task_repository import ITaskRepository
from src.core.entities.task import Task
from src.infrastructure.persistence.models.task import Task as TaskModel


class TaskRepository(ITaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, task: Task) -> Task:
        task_db = TaskModel(
            title=task.title,
            description=task.description,
            start=task.start,
            end=task.end,
            user_id=task.user_id,
            status_id=task.status_id
        )
        self.session.add(task_db)
        self.session.commit()
        self.session.refresh(task_db)
        return Task(
            id=task_db.id,
            title=task_db.title,
            description=task_db.description,
            start=task_db.start,
            end=task_db.end,
            user_id=task_db.user_id,
            status_id=task_db.status_id
        )

    def find_by_id(self, id: int) -> Optional[Task]:
        task_db = self.session.get(TaskModel, id)
        return Task(
            id=task_db.id,
            title=task_db.title,
            description=task_db.description,
            start=task_db.start,
            end=task_db.end,
            user_id=task_db.user_id,
            status_id=task_db.status_id
        ) if task_db else None

    def list_all(self) -> List[Task]:
        tasks_db = self.session.scalars(select(TaskModel)).all()
        return list(map(lambda task: Task(
            id=task.id,
            title=task.title,
            description=task.description,
            start=task.start,
            end=task.end,
            user_id=task.user_id,
            status_id=task.status_id
        ), tasks_db))

    def delete(self, id: int) -> None:
        task_db = self.session.get(TaskModel, id)
        self.session.delete(task_db)
        self.session.commit()

    def update(self, id: int, data: Dict[str, Any]) -> Task:
        task_db = self.session.get(TaskModel, id)
        for key, value in data.items():
            setattr(task_db, key, value)
        self.session.commit()
        self.session.refresh(task_db)
        return Task(
            id=task_db.id,
            title=task_db.title,
            description=task_db.description,
            start=task_db.start,
            end=task_db.end,
            user_id=task_db.user_id,
            status_id=task_db.status_id
        )

    def filter_by(self, filter_dict: Dict[str, Any]) -> List[Task]:
        tasks_db = self.session.scalars(select(TaskModel).filter_by(**filter_dict)).all()
        return list(map(lambda task: Task(
            id=task.id,
            title=task.title,
            description=task.description,
            start=task.start,
            end=task.end,
            user_id=task.user_id,
            status_id=task.status_id
        ), tasks_db))
