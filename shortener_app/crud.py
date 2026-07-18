# Handles all database (CRUD) operations for the application.

from sqlalchemy import select
from sqlalchemy.orm import Session

from shortener_app.models import URL
from shortener_app.schemas import URLCreate
from shortener_app.utils import (generate_secret_key, generate_unique_key,)
from shortener_app import exceptions
from shortener_app.logs import logger


def create_short_url(db: Session, url: URLCreate) -> URL:

    if url.custom_key:

        existing = get_url_by_key(db, url.custom_key)

        if existing:
            exceptions.custom_key_exists()

        key = url.custom_key

    else:
        key = generate_unique_key(db)

    db_url = URL(
        key=key,
        secret_key=generate_secret_key(db),
        target_url=str(url.target_url),
    )

    db.add(db_url)
    db.commit()
    logger.info(f"Created short URL '{db_url.key}'")
    db.refresh(db_url)

    return db_url


def get_url_by_key(db: Session, url_key: str) -> URL | None:

    statement = select(URL).where(URL.key == url_key)
    result = db.execute(statement)
    db_url = result.scalar_one_or_none()

    return db_url


def increment_clicks(db: Session, db_url: URL) -> None:
    db_url.clicks += 1
    db.commit()
    logger.info(f"Redirected '{db_url.key}'")


def deactivate_url(db: Session, secret_key: str) -> URL | None:

    statement = select(URL).where(URL.secret_key == secret_key)
    result = db.execute(statement)
    db_url = result.scalar_one_or_none()

    if db_url is None:
        return None

    db_url.is_active = False

    db.commit()
    
    logger.info(f"Deactivated '{db_url.key}'")

    db.refresh(db_url)

    return db_url