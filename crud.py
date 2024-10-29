# crud.py
from sqlalchemy.orm import Session
import models, schemas

def get_migrations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Migration).order_by(models.Migration.timestamp.desc()).offset(skip).limit(limit).all()

def create_migration(db: Session, migration: schemas.MigrationCreate):
    db_migration = models.Migration(**migration.dict())
    db.add(db_migration)
    db.commit()
    db.refresh(db_migration)
    return db_migration
