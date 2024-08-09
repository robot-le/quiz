import datetime
from pydantic import BaseModel, Field
from typing import Generic, TypeVar, Literal, Self

T = TypeVar('T')


class UserLogin(BaseModel):
    username: str
    password: str


class ResponseBase(BaseModel):
    status: Literal['success', 'error'] = 'success'
    detail: str


class ResponseBaseWithObject(ResponseBase, Generic[T]):
    obj: T


class UserBase(BaseModel):
    id: int | None = None
    username: str = Field(max_length=32)


class User(UserBase):
    pass

class Session(BaseModel):
    session_id: str
    expires_at: datetime.datetime
    user: User