from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from app.auth.jwt_handler import verify_token
from app.config import settings
from app.modules.ia_local import OllamaEngine
from app.modules.ia_remote import OpenAIEngine
from app.utils.logger import logger

router = APIRouter(prefix="/alexa", tags=["alexa"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_engine():
    if settings.ai_engine == "openai":
        return OpenAIEngine()
    elif settings.ai_engine == "ollama":
        return OllamaEngine()
    else:
        raise HTTPException(status_code=400, detail="Motor IA no soportado")

@router.post("/")
async def alexa_handler(request: Request, token: str = Depends(oauth2_scheme)):
    verify_token(token)
    data = await request.json()

    try:
        user_query = data["request"]["intent"]["slots"]["query"]["value"]
    except KeyError:
        raise HTTPException(status_code=400, detail="Formato inválido de consulta Alexa")

    engine = get_engine()
    ai_reply = engine.query(user_query)

    logger.info(f"Consulta Alexa procesada con motor {settings.ai_engine}")

    return JSONResponse({
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": ai_reply
            },
            "shouldEndSession": False
        }
    })
