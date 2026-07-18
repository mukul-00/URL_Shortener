
# Think of it as a fake browser
from fastapi.testclient import TestClient

from shortener_app.main import app


client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_create_url():

    response = client.post("/url", json={"target_url":"https://google.com"})

    assert response.status_code == 200

    data = response.json()

    assert data["target_url"] == "https://google.com/"


def test_stats():

    create = client.post("/url", json={"target_url":"https://youtube.com"})

    key = create.json()["key"]

    stats = client.get(f"/url/{key}/stats")

    assert stats.status_code == 200

    data = stats.json()

    assert data["key"] == key
    assert data["clicks"] == 0

def test_redirect():

    response = client.post("/url", json={"target_url": "https://github.com"})

    key = response.json()["key"]

    redirect = client.get(f"/{key}" ,follow_redirects=False)

    assert redirect.status_code in (307, 302)


def test_deactivate():

    response = client.post("/url", json={"target_url": "https://python.org"})

    secret_key = response.json()["secret_key"]

    delete = client.delete(f"/admin/{secret_key}")

    assert delete.status_code == 200


def test_deactivated_url_cannot_redirect():

    response = client.post("/url", json={"target_url": "https://openai.com"})

    data = response.json()

    client.delete(f"/admin/{data['secret_key']}")

    redirect = client.get(f"/{data['key']}", follow_redirects=False)

    assert redirect.status_code == 410