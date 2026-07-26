import pytest
from app.auth.jwt_handler import create_token, verify_token
from fastapi.testclient import TestClient
from app.main import app


# Test the JWT token creation and verification
def test_create_and_verify_token():
    token = create_token("test_user")
    payload = verify_token(token)
    assert payload["user_id"] == "test_user"


# Test the /auth/login endpoint
client = TestClient(app)

def test_login_success():
    response = client.post(
        "/auth/login",
        data={"username": "admin", "password": "1234"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_failure():
    response = client.post(
        "/auth/login",
        data={"username": "admin", "password": "wrong"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Credenciales inválidas"

# Test the /auth/register endpoint
def test_register():
    response = client.post(
        "/auth/register",
        params={"username": "nuevo_user", "password": "pass123"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Usuario nuevo_user registrado correctamente"
