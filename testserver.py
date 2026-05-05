import pytest
from server import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_returns_200(client):
    res = client.get("/")
    assert res.status_code == 200

def test_home_returns_ok_status(client):
    res = client.get("/")
    data = res.get_json()
    assert data["status"] == "ok"

def test_health_returns_200(client):
    res = client.get("/health")
    assert res.status_code == 200

def test_health_has_uptime(client):
    res = client.get("/health")
    data = res.get_json()
    assert "uptime_seconds" in data
    assert data["uptime_seconds"] >= 0

def test_error_returns_500(client):
    res = client.get("/error")
    assert res.status_code == 500
