from pwdlib import PasswordHash
from src.core.services.password_hasher import IPasswordHasher


class PasswordHasher(IPasswordHasher):
    def __init__(self):
        self.password_hash = PasswordHash.recommended()

    def hash_password(self, password: str) -> str:
        return self.password_hash.hash(password)

    def verify(self, password: str, hashed: str) -> bool:
        return self.password_hash.verify(password, hashed)
