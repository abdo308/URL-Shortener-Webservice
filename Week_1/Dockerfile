# Stage 1: Build stage - Install dependencies
FROM python:3.9-alpine AS builder

# Set working directory
WORKDIR /app

# Install build tools (Alpine uses apk instead of apt-get)
RUN apk add --no-cache \
    build-base gcc musl-dev

# Copy requirements
COPY requirements.txt .

# Install dependencies into a separate directory
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Production stage - Runtime image
FROM python:3.9-alpine AS production

# Set working directory
WORKDIR /app

# Copy installed Python packages from builder
COPY --from=builder /install /usr/local

# Copy only Python source files (avoids __pycache__)
COPY app/*.py app/

# Create the data directory for database
RUN mkdir -p /app/data

# Expose app port
EXPOSE 8000

# Start app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
