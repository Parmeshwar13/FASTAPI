from pydantic import BaseModel
from typing import Optional

class BlogCreate(BaseModel):
    title:str
    body:str
    published_at:Optional[str]=None

    class Config:
        orm_mode = True
