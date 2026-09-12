# what the client is allowed to send.
from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    done: bool

    class Config:
        from_attributes = True