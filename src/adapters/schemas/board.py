from pydantic import BaseModel


class BoardBase(BaseModel):
    name: str
    user_id: int

class BoardCreate(BoardBase):
    pass

class BoardResponse(BoardBase):
    id: int

class BoardUpdate(BaseModel):
    id: int
    name: str
