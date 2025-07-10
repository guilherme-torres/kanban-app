from abc import ABC, abstractmethod
from typing import Dict, Any


class IJWTService(ABC):
    @abstractmethod
    def generate_token(self, payload: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def validate_token(self, token: str) -> bool:
        pass

    @abstractmethod
    def decode_token(self, token: str) -> Dict[str, Any]:
        pass
