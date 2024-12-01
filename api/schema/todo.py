from pydantic import BaseModel, Field
from typing import Optional
from tortoise.contrib.pydantic import pyydantic_model_creator

GetLocs = pyydantic_model_creator(None, name="Todo")

class PostLocs(BaseModel):
    task: str = Field(..., max_length=100)
    done:bool

class PutLocs(BaseModel):
    task: Optional[str] = Field(None, max_length=100)
    done: Optional[bool]