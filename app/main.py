from typing import Optional, List
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, utils, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from .routers import post, user, auth

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
	return {"message": " my API"}
