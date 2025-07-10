from src.core.use_cases.authenticate import AuthenticateUseCase
from src.adapters.schemas.auth import AuthCredentials, AuthResponse


class AuthController:
    def __init__(self, auth_use_case: AuthenticateUseCase):
        self.auth_use_case = auth_use_case

    def authenticate(self, credentials: AuthCredentials) -> AuthResponse:
        access_token = self.auth_use_case.execute(credentials.email, credentials.password)
        return AuthResponse(access_token=access_token)
