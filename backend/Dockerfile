FROM python:3.12

WORKDIR /app

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHON_PATH=/app

RUN pip install gunicorn==23.0.0

RUN pip install "poetry==1.8.3"

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-ansi --no-root


COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]
