FROM python:3.11-slim

WORKDIR /app

# Install deps in a separate layer for cache efficiency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Run as non-root user (security best practice)
RUN useradd -m appuser
USER appuser

EXPOSE 3000

# Use gunicorn for production (not Flask's dev server)
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", \
     "--workers", "2", "--timeout", "30", "app:app"]