from pydantic import BaseModel, EmailStr


class AuthCredentials(BaseModel):
    email: EmailStr
    password: str

class AuthResponse(BaseModel):
    access_token: str
