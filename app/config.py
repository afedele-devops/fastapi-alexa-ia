from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Nombre de la aplicación
    app_name: str = "fastapi-alexa-ia"

    # Selección de motor IA
    ai_engine: str = "ollama"

    # Configuración OpenAI
    openai_api_key: str | None = None

    # Configuración Azure OpenAI
    azure_openai_endpoint: str | None = None
    azure_openai_key: str | None = None

    # Configuración Ollama
    ollama_host: str | None = None
    ollama_model: str = "llama2"

    # Endpoints y credenciales de desarrollo
    expose_config_endpoint: bool = False
    demo_username: str = "admin"
    demo_password: str = "1234"

    # Seguridad JWT
    jwt_secret: str = "change-me"

settings = Settings()
