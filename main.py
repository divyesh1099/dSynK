# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, models, schemas, git_monitor
from database import SessionLocal, engine
import asyncio

app = FastAPI()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to list migrations
@app.get("/migrations/", response_model=list[schemas.MigrationOut])
def list_migrations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_migrations(db, skip=skip, limit=limit)

# Periodic migration checker function
async def periodic_migration_checker():
    while True:
        db = SessionLocal()
        git_monitor.fetch_new_migrations(db)
        db.close()
        await asyncio.sleep(3600)  # Run every hour

# Startup event to begin the background task
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(periodic_migration_checker())
