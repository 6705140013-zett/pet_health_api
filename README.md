# Pet Health & Vaccine Tracker API (Python)

A Python REST API built with FastAPI and SQLite to manage pets and their vaccination timelines.

## Project Setup Instructions

### 1. Create and Activate Virtual Environment
```bash
python -m venv venv

pip install -r requirements.txt

---

#### 4. `database.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./pethealth.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
