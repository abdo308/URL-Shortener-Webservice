from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.endpoints import router
from app.database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager
    Creates database tables on startup
    """
    # Startup: Create database tables if they don't exist
    await create_tables()
    yield
    # Shutdown: Could add cleanup code here if needed

# Create FastAPI application instance with lifespan events
app = FastAPI(
    title="URL Shortener API",
    description="A simple URL shortener web service with SQLite storage",
    version="1.0.0",
    lifespan=lifespan
)

# Include the router with all endpoints
app.include_router(router)

@app.get("/")
async def root():
    """Root endpoint to check if the API is running"""
    return {
        "message": "URL Shortener API is running!",
        "version": "1.0.0",
        "storage": "SQLite Database",
        "endpoints": {
            "shorten_url": "POST /shorten",
            "redirect": "GET /{short_code}",
            "docs": "GET /docs"
        }
    }

