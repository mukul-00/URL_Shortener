# Provides reusable dependencies such as the database session.

from sqlalchemy.orm import Session

from shortener_app.database import SessionLocal


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

