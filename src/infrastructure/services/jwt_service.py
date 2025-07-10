from typing import Dict, Any
from datetime import datetime, timezone, timedelta
import jwt
from jwt.exceptions import (
    DecodeError,
    InvalidTokenError,
    InvalidSignatureError,
    ExpiredSignatureError,
)
from src.core.services.jwt_service import IJWTService
from src.infrastructure.config import JWTConfig


class JWTService(IJWTService):
    def __init__(self):
        self.config = JWTConfig()

    def generate_token(self, payload: Dict[str, Any]) -> str:
        expiration_time = datetime.now(tz=timezone.utc) + timedelta(
            seconds=self.config.JWT_EXPIRES_SECONDS
        )
        access_token = jwt.encode(
            {**payload, "exp": expiration_time},
            self.config.JWT_SECRET,
            self.config.JWT_ALGORITHM,
        )
        return access_token

    def validate_token(self, token: str) -> Any:
        try:
            decoded = jwt.decode(
                token, self.config.JWT_SECRET, algorithms=[self.config.JWT_ALGORITHM]
            )
            return decoded
        except ExpiredSignatureError:
            raise
        except InvalidSignatureError:
            raise
        except DecodeError:
            raise
        except InvalidTokenError:
            raise
