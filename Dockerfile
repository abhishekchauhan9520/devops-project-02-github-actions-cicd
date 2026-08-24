FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY sample_app ./sample_app

CMD ["python", "-m", "sample_app.app"]
