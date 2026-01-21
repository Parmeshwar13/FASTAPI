from fastapi import FastAPI,Depends
from . import models, schemas        # ✅ import BOTH
from .database import engine,SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

app=FastAPI()

@app.post('/blog_test')
def create_blog(title,body):
    return 'creating'

@app.post('/blog/')
def create_blog(request:schemas.BlogCreate,db:Session=Depends(get_db)):
    print(request.title,'debug')
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
