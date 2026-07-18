# Entry point of the FastAPI application.

from fastapi import Depends, FastAPI

from shortener_app.database import Base, engine
from shortener_app.models import URL

from shortener_app.routes.url import router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener API",
    description="A REST API for creating, managing, and redirecting shortened URLs.",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the URL Shortener API 🚀"
    }

