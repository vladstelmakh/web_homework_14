# app/schemas.py

from pydantic import BaseModel


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: str
    additional_data: str = None


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_verified: bool


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str
