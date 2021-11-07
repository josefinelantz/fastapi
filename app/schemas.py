from pydantic import BaseModel, EmailStr
from datetime import datetime

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
	# By default Pydantic works with dictionaries, so we tell it to be a model and not a dictionary
	class Config:
		orm_mode = True

class UserCreate(BaseModel):
	email: EmailStr
	password: str