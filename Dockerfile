FROM python:3.11-slim

# Create non-root user
RUN useradd -m app
WORKDIR /app

# Install dependencies (build cache-friendly)
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY --chown=app:app . /app
USER app

EXPOSE 8000

# Start the API (FastAPI assumed, using Uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
