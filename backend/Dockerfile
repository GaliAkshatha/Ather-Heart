FROM python:3.11-slim

# pytesseract is a wrapper around the system tesseract-ocr binary — it is
# NOT installed by pip. Without this, /api/ocr/upload will fail on any
# platform (like Render's native Python runtime) that doesn't already
# have tesseract-ocr installed.
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Don't ship dev-only artifacts into the image
RUN rm -rf model/training __pycache__ uploads/* venv 2>/dev/null || true

ENV PORT=5000
EXPOSE 5000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120"]
