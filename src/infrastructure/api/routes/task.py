from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.adapters.controllers.task_controller import TaskController
from src.core.use_cases.create_task import CreateTaskUseCase
from src.core.use_cases.list_user_tasks import ListUserTasksUseCase
from src.core.use_cases.update_task import UpdateTaskUseCase
from src.core.use_cases.delete_task import DeleteTaskUseCase
from src.core.use_cases.exceptions import UserNotFoundError, StatusNotFoundError, TaskNotFoundError, BoardNotFoundError
from src.infrastructure.persistence.repositories.task_repository import TaskRepository
from src.infrastructure.persistence.repositories.status_repository import StatusRepository
from src.infrastructure.persistence.repositories.user_repository import UserRepository
from src.infrastructure.persistence.repositories.board_repository import BoardRepository
from src.infrastructure.persistence.database.db import get_db_session
from src.adapters.schemas.task import TaskCreate, TaskResponse, TaskUpdate


router = APIRouter(prefix="/tasks")

def get_task_controller(db: Session):
    task_repository = TaskRepository(db)
    status_repository = StatusRepository(db)
    user_repository = UserRepository(db)
    board_repository = BoardRepository(db)
    create_task_use_case = CreateTaskUseCase(
        task_repository=task_repository,
        user_repository=user_repository,
        status_repository=status_repository,
        board_repository=board_repository,
    )
    list_user_tasks_use_case = ListUserTasksUseCase(
        user_repository=user_repository,
        task_repository=task_repository,
    )
    update_task_use_case = UpdateTaskUseCase(
        task_repository=task_repository,
        status_repository=status_repository,
    )
    delete_task_use_case = DeleteTaskUseCase(task_repository)
    return TaskController(
        create_task_use_case=create_task_use_case,
        list_user_tasks_use_case=list_user_tasks_use_case,
        update_task_use_case=update_task_use_case,
        delete_task_use_case=delete_task_use_case,
    )

@router.post("/", response_model=TaskResponse)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db_session)):
    try:
        task_controller = get_task_controller(db)
        return task_controller.create_task(task_data)
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    except StatusNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Status not found"
        )
    except BoardNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Board not found"
        )
    
@router.delete("/{id}")
def delete_task(id: int, db: Session = Depends(get_db_session)):
    try:
        task_controller = get_task_controller(db)
        return task_controller.delete_task(id)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    
@router.put("/{id}", response_model=TaskResponse)
def update_task(id: int, task_data: TaskUpdate, db: Session = Depends(get_db_session)):
    try:
        task_controller = get_task_controller(db)
        return task_controller.update_task(id, task_data)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    except StatusNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Status not found"
        )
    
@router.get("/", response_model=List[TaskResponse])
def list_user_tasks(user_id: int, db: Session = Depends(get_db_session)):
    try:
        task_controller = get_task_controller(db)
        return task_controller.list_user_tasks(user_id)
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
