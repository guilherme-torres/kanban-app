from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    user_id: Optional[int] = None
    status_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int