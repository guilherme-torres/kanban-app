from src.core.use_cases.create_user import CreateUserUseCase
from src.adapters.schemas.user import UserCreate, UserResponse
from src.core.entities.user import User


class UserController:
    def __init__(self, create_user_use_case: CreateUserUseCase):
        self.create_user_use_case = create_user_use_case

    def create_user(self, user_data: UserCreate) -> UserResponse:
        user = User(
            name=user_data.name,
            email=user_data.email,
            password=user_data.password,
        )
        created_user = self.create_user_use_case.execute(user)
        return UserResponse(
            id=created_user.id,
            name=created_user.name,
            email=created_user.email,
        )
