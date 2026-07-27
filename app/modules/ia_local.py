from fastapi import HTTPException
import requests
from app.config import settings
from app.utils.logger import logger
from app.modules.ia_engine import IAEngine

def query_ollama(model: str, prompt: str) -> str:
    """
    Envía una consulta al servidor Ollama y devuelve la respuesta del modelo.
    :param model: Nombre del modelo (ej. "llama2")
    :param prompt: Texto de entrada del usuario
    :return: Respuesta generada por el modelo
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt}
        )
        response.raise_for_status()
        data = response.json()

        # Ollama devuelve la respuesta bajo la clave "response"
        reply = data.get("response", "")
        if not reply:
            logger.warning("Ollama no devolvió respuesta")
            return "No se obtuvo respuesta del modelo."

        logger.info(f"Ollama respondió correctamente con modelo {model}")
        return reply

    except Exception as e:
        logger.error(f"Error en Ollama: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error en Ollama: {str(e)}")

class OllamaEngine(IAEngine):
    def query(self, prompt: str) -> str:
        return query_ollama(settings.ollama_model, prompt)