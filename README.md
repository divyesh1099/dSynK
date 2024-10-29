# DSynk

A lightweight, FastAPI-based tool for tracking database migration scripts in a Git repository. **DSynk** monitors changes in a specified repository's `migrations` folder, detects newly committed migration files, and logs them in a database, providing visibility into migration history over time.

## Features

- **Automatic Migration Tracking**: Detects new SQL migration scripts in the main branch and logs them with metadata such as author, commit message, and timestamp.
- **Commit Aggregation**: Combines multiple migration files from the same commit into a single entry for better readability.
- **Git Integration**: Uses GitPython to pull commit history and monitor changes in migration files.
- **API Endpoints**: Provides RESTful API endpoints to view migration history.
- **Periodic Background Task**: Continuously monitors the Git repository at set intervals for new migrations.

## Technologies Used

- **FastAPI** for building the API.
- **SQLAlchemy** for database management.
- **GitPython** for interacting with Git.
- **SQLite** as the default database.

---

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Git** installed and configured on your machine.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/migration-tracker.git
   cd migration-tracker
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Repository Path**:

   In `git_monitor.py`, set `REPO_PATH` to the absolute path of the Git repository you wish to monitor:

   ```python
   REPO_PATH = 'path/to/your/repo'
   ```

4. **Initialize the Database**:

   This project uses SQLite by default. The database will be automatically initialized when you start the app.

---

## Usage

### Running the FastAPI Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The application will run at `http://127.0.0.1:8000`.

### API Endpoints

- **List Migrations**: View migration history.
  
  ```
  GET /migrations/
  ```

  - **Query Parameters**:
    - `skip`: Number of entries to skip.
    - `limit`: Maximum number of entries to return.
  
- **Check Repository Status**: (Optional) Endpoint to verify Git repository setup.
  
  ```
  GET /repo_status/
  ```

### Background Task

The tool includes a periodic background task that checks for new migration scripts every hour. You can adjust this interval in `main.py`:

```python
await asyncio.sleep(3600)  # Check every hour
```

### Viewing the API Documentation

FastAPI provides automatic interactive documentation. Open the following link in your browser:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Testing

### Simulating Changes in the Repository

1. Add new migration files to the `migrations` directory in your Git repository.
2. Commit the changes:
   ```bash
   git add migrations/new_migration.sql
   git commit -m "Add new migration file"
   ```
3. The background task will detect the new migrations in the next cycle and log them in the database.

### Verifying Database Entries

Check the `migrations.db` SQLite file to confirm that migration entries are logged correctly:

```bash
sqlite3 migrations.db
SELECT * FROM migrations;
```

Alternatively, view the migration entries through the `/migrations/` API endpoint.

---

## Project Structure

```
migration-tracker/
├── main.py               # Entry point for FastAPI
├── models.py             # Database models
├── schemas.py            # Pydantic schemas for request/response
├── database.py           # Database configuration
├── crud.py               # CRUD operations for migrations
├── git_monitor.py        # Git monitoring and migration fetching
├── dependencies.py       # Dependencies for DB session and repo access
└── requirements.txt      # Project dependencies
```

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or suggestions, feel free to reach out!

**Author**: Divyesh Vishwakarma  
**Email**: [divyesh1099@gmail.com](mailto:divyesh1099@gmail.com)

