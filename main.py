from typing import Optional
from fastapi import FastAPI, Response, HTTPException, status
from fastapi.param_functions import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# Define schema for posts
class Post(BaseModel):
	title: str
	content: str
	published: bool = True
	rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "I like pizza", "id": 2}]

def find_post(id):
	for p in my_posts:
		if p["id"] == id:
			return p

def find_index_post(id):
	for i, p in enumerate(my_posts):
		if p["id"] == id:
			return i

# Route || Path operation is referenced by decorator @
@app.get("/")
async def root():
	# Return Python dictionary, FastAPI interprets it to JSON
	return {"message": " my API"}

@app.get("/posts")
def get_posts():
	# FastApi converts the array to JSON
	return{"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
#Take in payload validate according to post schema
def create_posts(post: Post):
	post_dict = post.dict()
	# Generate an id
	post_dict['id'] = randrange(0, 1000000)
	# Convert Post to a dictionary and append to array
	my_posts.append(post_dict)
	return{"data": post_dict}

@app.get("/posts/{id}")	
def get_post(id: int):
	post = find_post(id)
	if not post: 
		raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
	return{"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
	index = find_index_post(id) 
	if index == None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist ")
	my_posts.pop(index) 
	return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
	index = find_index_post(id) 
	if index == None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist ")
	# Convert data from frontend stored in post to dictionary
	post_dict = post.dict()
	# Set id inside new dictionary to the update id
	post_dict["id"] = id
	# set current post to the updated post 
	my_posts[index] = post_dict
	# return updated post
	return {"data": post_dict}