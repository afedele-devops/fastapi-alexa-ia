import pytest
from app.modules.ia_remote import OpenAIEngine

def test_openai_engine(monkeypatch):
    def mock_post(url, headers, json):
        class MockResponse:
            def raise_for_status(self): pass
            def json(self): return {"choices": [{"message": {"content": "Respuesta simulada"}}]}
        return MockResponse()
    monkeypatch.setattr("requests.post", mock_post)

    engine = OpenAIEngine()
    result = engine.query("Hola")
    assert result == "Respuesta simulada"
