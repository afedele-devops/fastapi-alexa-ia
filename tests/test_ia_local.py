import pytest
from fastapi import HTTPException
from app.modules.ia_local import OllamaEngine, query_ollama

def test_ollama_engine_success(monkeypatch):
    def mock_post(url, json):
        class MockResponse:
            def raise_for_status(self): pass
            def json(self): return {"response": "Respuesta simulada"}
        return MockResponse()
    monkeypatch.setattr("requests.post", mock_post)

    engine = OllamaEngine()
    result = engine.query("Hola")
    assert result == "Respuesta simulada"

def test_ollama_engine_empty_response(monkeypatch):
    def mock_post(url, json):
        class MockResponse:
            def raise_for_status(self): pass
            def json(self): return {"response": ""}
        return MockResponse()
    monkeypatch.setattr("requests.post", mock_post)

    result = query_ollama("llama2", "Hola")
    assert result == "No se obtuvo respuesta del modelo."

def test_ollama_engine_error(monkeypatch):
    def mock_post(url, json):
        raise Exception("Error de conexión")
    monkeypatch.setattr("requests.post", mock_post)

    with pytest.raises(HTTPException) as excinfo:
        query_ollama("llama2", "Hola")
    assert "Error en Ollama" in str(excinfo.value.detail)

def test_ollama_engine_http_exception(monkeypatch):
    def mock_post(url, json):
        class MockResponse:
            def raise_for_status(self): raise HTTPException(status_code=500, detail="Error de servidor")
        return MockResponse()
    monkeypatch.setattr("requests.post", mock_post)

    with pytest.raises(HTTPException) as excinfo:
        query_ollama("llama2", "Hola")
    assert "Error en Ollama" in str(excinfo.value.detail)

