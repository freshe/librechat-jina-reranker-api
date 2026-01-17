FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    SERVER_HOST=0.0.0.0 \
    SERVER_PORT=8000 \
    CACHE_DIR=/app/.cache

WORKDIR /app

RUN groupadd --system app && useradd --system --gid app --create-home app

COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app/
RUN chown -R app:app /app

USER app

EXPOSE 8000

CMD ["python", "main.py"]
