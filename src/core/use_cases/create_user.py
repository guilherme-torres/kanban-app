from src.core.repository_interfaces.user_repository import IUserRepository
from src.core.services.password_hasher import IPasswordHasher
from src.core.entities.user import User
from src.core.use_cases.exceptions import UserAlreadyExistsError


class CreateUserUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
        password_hasher: IPasswordHasher,
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, user: User) -> User:
        user_exist = self.user_repository.find_by_email(user.email)
        if user_exist:
            raise UserAlreadyExistsError("User already exists")
        user.password = self.password_hasher.hash_password(user.password)
        return self.user_repository.save(user)
