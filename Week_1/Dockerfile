# Multi-stage Docker build for URL Shortener

# Stage 1: Build stage - Install dependencies
FROM python:3.9-slim AS builder

# Set working directory
WORKDIR /app

# Install build tools (if needed for compiling deps)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install dependencies into a separate directory
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Production stage - Runtime image
FROM python:3.9-slim AS production

# Set working directory
WORKDIR /app

# Copy installed Python packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Expose app port
EXPOSE 8000

# Start app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
