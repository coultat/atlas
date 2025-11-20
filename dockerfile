FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Setze PYTHONPATH damit Python das src-Verzeichnis findet
ENV PYTHONPATH=/app/src

CMD ["uvicorn", "atlas.app.app:app", "--host", "0.0.0.0", "--port", "8000"]