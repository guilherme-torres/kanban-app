from pydantic import BaseModel


class StatusBase(BaseModel):
    name: str
    user_id: int
    board_id: int

class StatusCreate(StatusBase):
    pass

class StatusResponse(StatusBase):
    id: int