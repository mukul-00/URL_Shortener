# Handles all HTTP requests and responses related to URL shortening.

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from shortener_app import crud
from shortener_app.dependencies import get_db
from shortener_app.schemas import URLCreate, URLResponse
from shortener_app import exceptions

router = APIRouter()


@router.post("/url", response_model=URLResponse, summary="Create a short URL", tags=["URLs"],description="Creates a new shortened URL with either a random or custom key.")
def create_url(url: URLCreate, db: Session = Depends(get_db)):
    # Depends means = before running this function,please give me a database session.

    try:
        return crud.create_short_url(db, url)
    
    except ValueError:
        exceptions.custom_key_exists()


@router.get("/{url_key}", summary="Redirect to the original URL")
def redirect_to_url(url_key: str, db: Session = Depends(get_db)):

    db_url = crud.get_url_by_key(db, url_key)

    if db_url is None:
        exceptions.url_not_found()

    if not db_url.is_active:
        exceptions.url_inactive()

    crud.increment_clicks(db, db_url)

    # RedirectResponse is a FastAPI response that tells the browser to automatically visit another URL.
    # RedirectResponse redirects the user from one URL to another.
    return RedirectResponse(url=db_url.target_url, status_code=307)



@router.get("/url/{url_key}/stats", response_model=URLResponse, summary="Get URL statistics")
def get_url_stats(url_key: str, db: Session = Depends(get_db)):

    db_url = crud.get_url_by_key(db, url_key)

    if db_url is None:
        exceptions.url_not_found()

    return db_url


@router.delete("/admin/{secret_key}", response_model=URLResponse, summary="Deactivate a short URL")
def deactivate_url(secret_key: str, db: Session = Depends(get_db),):

    db_url = crud.deactivate_url(db, secret_key)

    if db_url is None:
        exceptions.url_not_found()

    return db_url