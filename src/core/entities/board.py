from dataclasses import dataclass
from typing import Optional


@dataclass
class Board:
    name: str
    user_id: int
    id: Optional[int] = None
