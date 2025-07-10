from src.core.repository_interfaces.user_repository import IUserRepository
from src.core.services.jwt_service import IJWTService
from src.core.services.password_hasher import IPasswordHasher
from src.core.use_cases.exceptions import ApplicationError, InvalidCredentialsError


class AuthenticateUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
        jwt_service: IJWTService,
        password_hasher: IPasswordHasher,
    ):
        self.user_repository = user_repository
        self.jwt_service = jwt_service
        self.password_hasher = password_hasher

    def execute(self, email: str, password: str) -> str:
        if not email or not password:
            raise ApplicationError("Credentials required")
        user = self.user_repository.find_by_email(email)
        if not user:
            raise InvalidCredentialsError("Invalid credentials")
        if not self.password_hasher.verify(password, user.password):
            raise InvalidCredentialsError("Invalid credentials")
        token = self.jwt_service.generate_token({"name": user.name, "user_id": user.id})
        return token
