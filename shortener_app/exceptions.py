# Contains reusable HTTP exceptions used throughout the application.

from fastapi import HTTPException

from shortener_app.logs import logger

def url_not_found():

    logger.warning("Requested URL was not found.")

    raise HTTPException(
        status_code=404,
        detail="URL not found"
    )


def url_inactive():
    raise HTTPException(
        status_code=410,
        detail="URL is inactive"
    )


def custom_key_exists():
    raise HTTPException(
        status_code=400,
        detail="Custom key already exists."
    )