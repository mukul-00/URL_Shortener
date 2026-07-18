# Creates and manages the database connection and sessions.

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from shortener_app.config import settings


class Base(DeclarativeBase):
    pass

# A connection between your FastAPI application and the database.
engine = create_engine(
    settings.db_url,
    connect_args={"check_same_thread": False}, # Meaning "It's okay if another thread uses this connection."
)


# A session is a conversation with the database.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False,) 

