from fastapi import FastAPI 
app = FastAPI()
from schema import Blog
from typing import Optional

@app.get('/')
def root():
    return {"message":"welcome to FastAPI"}


@app.get('/blog/')
def get_blogs(limit=10,published:Optional[bool]=None):
    if published:
      return {"data": f"{limit} published blogs:"}
    else:
        return {"data":f"{limit} blogs"}

@app.get('/blog/unpbulished')
def unpublished():
    return{'data':"unpublished blogs"}

@app.get("/blog/{id}")
def get_blog_by_id(id:int):
    return {"data":f"blog with id {id}"}


@app.get("/blog/{id}/comments")
def comments(id:int):
    return {'data':{'1','2'}}

@app.post('/blog/')
def create_blog(blog:Blog):
    return (f"{blog.title}-{blog.description}")

