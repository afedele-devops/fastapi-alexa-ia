import requests
from fastapi import HTTPException
from app.utils.logger import logger
from app.config import settings
from app.modules.ia_engine import IAEngine

def query_openai(model: str, prompt: str) -> str:
    """
    Envía una consulta al servicio OpenAI y devuelve la respuesta del modelo.
    :param model: Nombre del modelo (ej. "gpt-4")
    :param prompt: Texto de entrada del usuario
    :return: Respuesta generada por el modelo
    """
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.openai_api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        response.raise_for_status()
        data = response.json()

        # OpenAI devuelve la respuesta en choices[0].message.content
        reply = data["choices"][0]["message"]["content"]
        if not reply:
            logger.warning("OpenAI no devolvió respuesta")
            return "No se obtuvo respuesta del modelo remoto."

        logger.info(f"OpenAI respondió correctamente con modelo {model}")
        return reply

    except Exception as e:
        logger.error(f"Error en OpenAI: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error en OpenAI: {str(e)}")

class OpenAIEngine(IAEngine):
    def query(self, prompt: str) -> str:
        return query_openai("gpt-4", prompt)
    