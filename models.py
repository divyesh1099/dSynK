# models.py
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Migration(Base):
    __tablename__ = 'migrations'
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    author = Column(String)
    commit_message = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

DATABASE_URL = "sqlite:///./migrations.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
