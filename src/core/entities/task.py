from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    title: str
    description: str
    start: datetime
    end: datetime
    user_id: int
    status_id: int
    id: Optional[int] = None
