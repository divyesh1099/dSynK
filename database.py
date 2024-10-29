# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your database URL here. 
# Change this to your preferred database URL if not using SQLite.
DATABASE_URL = "sqlite:///./migrations.db"

# Create a database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Function to initialize the database, if necessary
def init_db():
    Base.metadata.create_all(bind=engine)
