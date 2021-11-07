from typing import Optional, List
from fastapi import FastAPI, Response, HTTPException, status, Depends
from fastapi.param_functions import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# while True:
# 	try: 
# 		conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="root", cursor_factory=RealDictCursor)
# 		cursor = conn.cursor()
# 		print("Database connection was successful")
# 		break
# 	except Exception as error: 
# 		print("Connection failed")
# 		print("error: ", error)
# 		time.sleep(2)

# Route || Path operation is referenced by decorator @
@app.get("/")
async def root():
	# Return Python dictionary, FastAPI interprets it to JSON
	return {"message": " my API"}

@app.get("/posts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
	posts = db.query(models.Post).all()
	# cursor.execute("""select * from posts """)
	# posts = cursor.fetchall()

	# FastApi converts the array to JSON
	return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
#Take in payload validate according to post schema
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
	# cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))

	# new_post = cursor.fetchone()
	# conn.commit()
	new_post = models.Post(**post.dict())
	db.add(new_post)
	db.commit()
	db.refresh(new_post)
	return new_post

@app.get("/posts/{id}", response_model=schemas.Post)	
def get_post(id: int, db: Session = Depends(get_db)):
	# cursor.execute(""" SELECT * from posts 
	# WHERE id = %s """, (str(id)))
	# post = cursor.fetchone()
	post = db.query(models.Post).filter(models.Post.id == id).first()

	if not post: 
		raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
	return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
	# cursor.execute(""" DELETE from posts WHERE id = %s RETURNING * """, (str(id)))
	# deleted_post = cursor.fetchone()
	# conn.commit()
	post = db.query(models.Post).filter(models.Post.id == id)
	if post.first() == None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist ")
	post.delete(synchronize_session = False)
	db.commit()
	return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
	# cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, str(id)))
	# updated_post = cursor.fetchone()
	# conn.commit()
	post_query = db.query(models.Post).filter(models.Post.id == id)

	post = post_query.first() 

	if post == None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist ")
	
	post_query.update(updated_post.dict(), synchronize_session=False)
	db.commit()
	# return updated post
	return post_query.first()
	
@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
	posts = db.query(models.Post).all()
	return posts

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
	new_user = models.User(**user.dict())
	db.add(new_user)
	db.commit()
	db.refresh(new_user)

	return new_user
