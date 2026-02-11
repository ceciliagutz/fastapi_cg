#project CG

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}

def test_get_all_users():
    response = client.get("/user/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(emp["first_name"] == "Cecilia" for emp in data)

def test_get_active_users():
    response = client.get("/user/active?is_active=true")
    assert response.status_code == 200
    data = response.json()
    assert all(emp["is_active"] for emp in data)

def test_get_inactive_users():
    response = client.get("/user/active?is_active=false")
    assert response.status_code == 200
    data = response.json()
    assert all(not emp["is_active"] for emp in data)

def test_create_user():
    new_user = {
        "first_name": "Paula",
        "last_name": "Martinion",
        "position": "System ",
        "email": "paula.martinion@example.com",
        "is_active": True
    }
    response = client.post("/user/", json=new_user)
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Paula"
