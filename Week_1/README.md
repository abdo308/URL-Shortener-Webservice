# URL Shortener Web Service

A FastAPI-based URL shortener service with SQLite storage.

## Running the Application

You have two options to run this application:

### Option 1: Using Docker (Recommended)

If you prefer to run the application using Docker:

#### Prerequisites
- Docker installed on your system

#### Steps
1. **Build the Docker image:**
   ```bash
   docker build -t url-shortener .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 8000:8000 url-shortener
   ```

The application will be available at `http://localhost:8000`

### Option 2: Local Development Setup

If you want to build and run locally:

#### Prerequisites
- Python 3.9 or higher
- pip package manager

#### Steps
1. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

The application will be available at `http://localhost:8000`

## API Endpoints

Once the application is running, you can:

- **View API documentation:** `http://localhost:8000/docs`
