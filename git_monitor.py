# git_monitor.py
from git import Repo

from crud import create_migration
import crud
import models
from schemas import MigrationCreate
from sqlalchemy.orm import Session
import os
import datetime

# Path to your repo (adjust as needed)
REPO_PATH = r'D:\Divyesh\NeuralIT\dummyMigrationsRepo'

def fetch_new_migrations(db: Session):
    repo = Repo(REPO_PATH)
    commits = list(repo.iter_commits('main', max_count=10))

    for commit in commits:
        print(f"Checking commit: {commit.hexsha}, Message: {commit.message}")
        
        # Collect all migration files in this commit
        migration_files = []
        for file_path in commit.stats.files.keys():
            print(f"File in commit: {file_path}")
            if "migrations/" in file_path and file_path.endswith(".sql"):
                migration_files.append(file_path)

        # Only add to DB if there are migration files in this commit
        if migration_files:
            # Convert list of filenames into a single string, separated by commas
            filenames = ', '.join(migration_files)
            print(f"New migration detected for commit: {filenames}")

            # Create a single migration entry for this commit
            migration = MigrationCreate(
                filename=filenames,
                author=commit.author.name,
                commit_message=commit.message,
                timestamp=datetime.datetime.fromtimestamp(commit.committed_date)
            )

            # Check if this commit (by timestamp and commit message) is already in the DB
            existing_migration = db.query(models.Migration).filter_by(
                commit_message=migration.commit_message.strip(),
                timestamp=migration.timestamp
            ).first()
            
            if not existing_migration:
                print(f"Adding aggregated migration to database for commit: {filenames}")
                crud.create_migration(db, migration)
            else:
                print(f"Migration for commit {commit.hexsha} already exists in the database.")