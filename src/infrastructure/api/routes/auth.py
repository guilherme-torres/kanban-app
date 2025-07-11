from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.adapters.controllers.auth_controller import AuthController
from src.core.use_cases.authenticate import AuthenticateUseCase
from src.infrastructure.persistence.repositories.user_repository import UserRepository
from src.infrastructure.services.password_hasher import PasswordHasher
from src.infrastructure.services.jwt_service import JWTService
from src.infrastructure.persistence.database.db import get_db_session
from src.adapters.schemas.auth import AuthCredentials, AuthResponse
from src.core.use_cases.exceptions import InvalidCredentialsError


router = APIRouter(prefix="/token")

def get_auth_controller(db: Session):
    user_repository = UserRepository(db)
    password_hasher = PasswordHasher()
    jwt_service = JWTService()
    auth_use_case = AuthenticateUseCase(
        user_repository=user_repository,
        jwt_service=jwt_service,
        password_hasher=password_hasher,
    )
    return AuthController(auth_use_case)

@router.post("/", response_model=AuthResponse)
def generate_token(credendials: AuthCredentials, db: Session = Depends(get_db_session)):
    try:
        auth_controller = get_auth_controller(db)
        return auth_controller.authenticate(credendials)
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials"
        )
