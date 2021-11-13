from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
	email: EmailStr
	password: str

class UserOut(BaseModel):
	id: int
	email: EmailStr
	created_at: datetime

	class Config:
		orm_mode=True

class UserLogin(BaseModel):
	email: EmailStr
	password: str
# Define Pydantic model(schema) for posts as python classes
class PostBase(BaseModel):
	title: str
	content: str
	published: bool = True

class PostCreate(PostBase):
	pass

class Post(PostBase):
	id: int
	created_at: datetime
	owner_id: int
	owner: UserOut
	# By default Pydantic works with dictionaries, so we tell it to be a model and not a dictionary
	class Config:
		orm_mode = True

class Token(BaseModel):
	access_token: str
	token_type: str

class TokenData(BaseModel):
	id: Optional[str] = None
