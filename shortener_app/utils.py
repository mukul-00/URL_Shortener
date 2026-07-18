# Contains helper functions used throughout the application.

import secrets
import string

from sqlalchemy import select
from sqlalchemy.orm import Session

from shortener_app.models import URL


KEY_LENGTH = 6
SECRET_KEY_LENGTH = 16


def create_random_key(length: int = KEY_LENGTH) -> str:

    # string.ascii_letters => It gives :- abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    # string.digits => It gives :- 0123456789
    characters = string.ascii_letters + string.digits

    letters = []

    for _ in range(length):
        letters.append(secrets.choice(characters))

    return "".join(letters)


def generate_unique_key(db: Session) -> str:
    while True:
        key = create_random_key()

        # SELECT * FROM urls
        # WHERE key = 'Ab7P2X';
        statement = select(URL).where(URL.key == key)

        existing = db.execute(statement).scalar_one_or_none()

        if existing is None:
            return key


def generate_secret_key(db: Session) -> str:
    while True:
        key = create_random_key(SECRET_KEY_LENGTH)

        statement = select(URL).where(URL.secret_key == key)

        existing = db.execute(statement).scalar_one_or_none()

        if existing is None:
            return key