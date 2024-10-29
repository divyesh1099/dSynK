# schemas.py
from pydantic import BaseModel
from datetime import datetime

class MigrationCreate(BaseModel):
    filename: str
    author: str
    commit_message: str
    timestamp: datetime

class MigrationOut(MigrationCreate):
    id: int
    class Config:
        from_attributes = True
