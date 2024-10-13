FROM python:3.10

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml ./pyproject.toml

RUN poetry install

COPY . .

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
