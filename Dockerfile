# syntax=docker/dockerfile:1
# -----------------------------------------------------------------------------
#  RHCert-Viewer Container Image
# -----------------------------------------------------------------------------
#  • Uses a minimal slim Python base image
#  • Runs the Flask application via Gunicorn
#  • Drops privileges to non-root user for security
# -----------------------------------------------------------------------------

FROM python:3.12-slim AS base

# Install system dependencies if needed (none for now)
# RUN apt-get update && apt-get install -y --no-install-recommends ... && rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------------------------------
# Create application user (non-root)
# -----------------------------------------------------------------------------
RUN useradd -m viewer
WORKDIR /home/viewer

# -----------------------------------------------------------------------------
# Copy application code & install Python dependencies
# -----------------------------------------------------------------------------
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Gunicorn will run on port 8080 inside the container
EXPOSE 8080

USER viewer

# -----------------------------------------------------------------------------
# Start Gunicorn with 3 worker processes.
# Increase workers (or switch to async workers) if you expect high concurrency.
# -----------------------------------------------------------------------------
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "3", "web_server:app"]