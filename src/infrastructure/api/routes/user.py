from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.adapters.controllers.user_controller import UserController
from src.core.use_cases.create_user import CreateUserUseCase
from src.core.use_cases.exceptions import UserAlreadyExistsError
from src.infrastructure.persistence.repositories.user_repository import UserRepository
from src.infrastructure.persistence.database.db import get_db_session
from src.adapters.schemas.user import UserCreate, UserResponse
from src.infrastructure.services.password_hasher import PasswordHasher


router = APIRouter(prefix="/users")

def get_user_controller(db: Session):
    user_repository = UserRepository(db)
    password_hasher = PasswordHasher()
    create_user_case = CreateUserUseCase(
        user_repository=user_repository,
        password_hasher=password_hasher
    )
    user_controller = UserController(create_user_case)
    return user_controller

@router.post("/", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db_session)):
    try:
        user_controller = get_user_controller(db)
        return user_controller.create_user(user_data)
    except UserAlreadyExistsError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
