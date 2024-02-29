from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "FastAPI"}


def test_read_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"detail": "ok"}