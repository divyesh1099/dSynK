# dependencies.py
from sqlalchemy.orm import Session
from .database import SessionLocal
from fastapi import Depends, HTTPException
from git import Repo
import os

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to access the Git repository
def get_repo():
    # Set this to your repository path
    REPO_PATH = r'D:\Divyesh\NeuralIT\dummyMigrationsRepo'
    
    if not os.path.isdir(REPO_PATH):
        raise HTTPException(status_code=404, detail="Git repository not found.")
    
    repo = Repo(REPO_PATH)
    if repo.bare:
        raise HTTPException(status_code=500, detail="Repository is bare and cannot be accessed.")
    
    return repo
