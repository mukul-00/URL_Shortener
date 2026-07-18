# URL Shortener API
A REST API built with FastAPI for creating and managing shortened URLs.


## Features
- Create short URLs
- Redirect to original URLs
- URL statistics
- Custom short keys
- Deactivate URLs using a secret key
- Logging
- Automated tests
- Docker support


## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- Docker


## Project Structure
url_shortener_project/
│
├── shortener_app/
├── tests/
├── Dockerfile
├── requirements.txt
├── run.py
└── README.md


## Installation
git clone <repository-url>
cd url-shortener
python -m venv venv


# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
python run.py

## Docker
docker build -t url-shortener .
docker run -p 8000:8000 url-shortener

## Testing
python -m pytest


## Documentation
http://localhost:8000/docs

