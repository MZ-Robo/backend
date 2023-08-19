from pydantic import BaseModel, validator
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str
    password_confirm: str

    @validator("password_confirm")
    def passwords_match(cls, password_confirm, values, **kwargs):
        if "password" in values and password_confirm != values["password"]:
            raise ValueError("password and password_confirm do not match")
        return password_confirm


class User(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
