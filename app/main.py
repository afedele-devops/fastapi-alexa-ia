from fastapi import FastAPI
from app.config import settings
from app.auth import routes as auth_routes
from app.modules import alexa

app = FastAPI(title=settings.app_name)

# Registrar routers
app.include_router(auth_routes.router)
app.include_router(alexa.router)

if settings.expose_config_endpoint:
    # Endpoint de diagnóstico sólo cuando se habilita explícitamente
    @app.get("/config")
    def get_config():
        return {
            "app_name": settings.app_name,
            "ai_engine": settings.ai_engine,
            "ollama_host": settings.ollama_host,
            "openai_api_key": "****" if settings.openai_api_key else None,
            "azure_openai_endpoint": settings.azure_openai_endpoint,
        }
