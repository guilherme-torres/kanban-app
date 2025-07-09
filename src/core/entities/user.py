from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    name: str
    email: str
    password: str
    id: Optional[int] = None
