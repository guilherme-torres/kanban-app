from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    title: str
    user_id: int
    status_id: int
    board_id: int
    description: Optional[str] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    id: Optional[int] = None
