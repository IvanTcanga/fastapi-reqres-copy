from pydantic import BaseModel
from datetime import datetime


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str


class UserResponse(BaseModel):
    data: UserData
    support: Support


class UserCreateRequest(BaseModel):
    name: str
    job: str


class UserCreateResponse(BaseModel):
    name: str
    job: str
    id: int
    createdAt: datetime
