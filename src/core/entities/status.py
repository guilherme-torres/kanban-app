from dataclasses import dataclass
from typing import Optional


@dataclass
class Status:
    name: str
    user_id: int
    id: Optional[int] = None
