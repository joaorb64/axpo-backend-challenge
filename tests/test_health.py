from fastapi.testclient import TestClient
from app.main import app as main_app

client = TestClient(main_app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
