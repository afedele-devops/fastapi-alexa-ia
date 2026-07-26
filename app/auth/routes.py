from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.jwt_handler import create_token
from app.config import settings
from app.utils.logger import logger
from secrets import compare_digest

router = APIRouter(prefix="/auth", tags=["auth"])

# Endpoint de login
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint de autenticación.
    Recibe username y password, valida credenciales y devuelve un JWT.
    """
    username = form_data.username
    password = form_data.password

    # Credenciales de desarrollo; en producción sustituir por validación real
    username_matches = compare_digest(username, settings.demo_username)
    password_matches = compare_digest(password, settings.demo_password)

    if username_matches and password_matches:
        token = create_token(user_id=username)
        logger.info(f"Usuario {username} autenticado correctamente")
        return {"access_token": token, "token_type": "bearer"}
    else:
        logger.warning(f"Intento de login fallido para usuario {username}")
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

# Endpoint opcional de registro (mock)
@router.post("/register")
def register(username: str, password: str):
    """
    Endpoint de registro de usuario.
    En un caso real, deberías guardar el usuario en la base de datos.
    """
    logger.info(f"Usuario {username} registrado (mock)")
    return {"message": f"Usuario {username} registrado correctamente"}
