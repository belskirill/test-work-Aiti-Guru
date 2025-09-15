FROM python:3.12-slim

# Установка системных зависимостей (включая sqlite3)
RUN apt-get update && apt-get install -y \
    curl build-essential sqlite3 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Установка poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /app
ENV PYTHONPATH=/app

# Установка зависимостей
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копируем код
COPY . .

# Запуск приложения через uvicorn
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
