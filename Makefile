# Variables
APP=app.main:app
PORT=8000
PYTHON=.venv/bin/python
UVICORN=.venv/bin/uvicorn

# Instalar dependencias
install:
	$(PYTHON) -m pip install -r requirements.txt

# Ejecutar servidor FastAPI
run:
	$(UVICORN) $(APP) --reload --port $(PORT)

# Ejecutar pruebas unitarias
test:
	$(PYTHON) -m pytest -v

# Construir imagen Docker
docker-build:
	docker-compose build

# Levantar servicios Docker
docker-up:
	docker-compose up -d

# Apagar servicios Docker
docker-down:
	docker-compose down

# Limpiar contenedores e imágenes
docker-clean:
	docker-compose down --rmi all --volumes --remove-orphans
