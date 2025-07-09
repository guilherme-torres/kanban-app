from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.adapters.controllers.status_controller import StatusController
from src.core.use_cases.create_status import CreateStatusUseCase
from src.core.use_cases.delete_status import DeleteStatusUseCase
from src.core.use_cases.list_user_status import ListUserStatusUseCase
from src.core.use_cases.exceptions import UserNotFoundError, StatusNotFoundError
from src.infrastructure.persistence.repositories.status_repository import StatusRepository
from src.infrastructure.persistence.repositories.user_repository import UserRepository
from src.infrastructure.persistence.database.db import get_db_session
from src.adapters.schemas.status import StatusCreate, StatusResponse


router = APIRouter(prefix="/status")


def get_status_controller(db: Session):
    status_repository = StatusRepository(db)
    user_repository = UserRepository(db)
    create_status_use_case = CreateStatusUseCase(
        status_repository=status_repository, user_repository=user_repository
    )
    delete_status_use_case = DeleteStatusUseCase(status_repository)
    list_user_status_use_case = ListUserStatusUseCase(
        status_repository=status_repository, user_repository=user_repository
    )
    return StatusController(
        create_status_use_case,
        delete_status_use_case,
        list_user_status_use_case,
    )


@router.post("/", response_model=StatusResponse)
def create_status(status_data: StatusCreate, db: Session = Depends(get_db_session)):
    try:
        status_controller = get_status_controller(db)
        return status_controller.create_status(status_data)
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User not found"
        )
    
@router.delete("/{id}")
def delete_status(id: int, db: Session = Depends(get_db_session)):
    try:
        status_controller = get_status_controller(db)
        return status_controller.delete_status(id)
    except StatusNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Status not found"
        )
    
@router.get("/", response_model=List[StatusResponse])
def list_user_status(user_id: int, db: Session = Depends(get_db_session)):
    try:
        status_controller = get_status_controller(db)
        return status_controller.list_user_status(user_id)
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User not found"
        )
