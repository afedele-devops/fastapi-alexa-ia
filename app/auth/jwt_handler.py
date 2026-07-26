import time
import jwt
from fastapi import HTTPException
from app.config import settings
from app.utils.logger import logger

# Tiempo de expiración del token (ejemplo: 1 hora)
TOKEN_EXPIRATION = 3600  

def create_token(user_id: str) -> str:
    """
    Genera un JWT para el usuario dado.
    :param user_id: Identificador único del usuario
    :return: Token JWT firmado
    """
    try:
        payload = {
            "user_id": user_id,
            "exp": time.time() + TOKEN_EXPIRATION
        }
        token = jwt.encode(payload, settings.jwt_secret, algorithm="HS256")
        logger.info(f"Token JWT generado para usuario {user_id}")
        return token
    except Exception as e:
        logger.error(f"Error generando token JWT: {str(e)}")
        raise HTTPException(status_code=500, detail="Error generando token JWT")

def verify_token(token: str) -> dict:
    """
    Verifica un JWT y devuelve el payload si es válido.
    :param token: Token JWT recibido
    :return: Payload decodificado
    """
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        logger.info(f"Token JWT verificado correctamente para usuario {payload['user_id']}")
        return payload
    except jwt.ExpiredSignatureError:
        logger.warning("Token JWT expirado")
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        logger.warning("Token JWT inválido")
        raise HTTPException(status_code=401, detail="Token inválido")
