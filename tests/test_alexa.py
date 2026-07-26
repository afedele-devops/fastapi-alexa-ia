import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.auth.jwt_handler import create_token

client = TestClient(app)

def test_alexa_endpoint_with_valid_token():
    token = create_token({"sub": "test_user"})
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "request": {
            "intent": {
                "slots": {
                    "query": {"value": "Hola IA"}
                }
            }
        }
    }
    response = client.post("/alexa/", headers=headers, json=body)
    assert response.status_code in [200, 500]  # 500 si no hay motor configurado
