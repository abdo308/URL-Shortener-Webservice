#!/usr/bin/env python3
"""
Script to run the URL Shortener API server
"""

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Starting URL Shortener API...")
    print("📡 Server will be available at: http://localhost:8000")
    print("📚 API documentation at: http://localhost:8000/docs")
    print("🔄 Press CTRL+C to stop\n")
    
    # Run the FastAPI application
    uvicorn.run(
        "app.main:app",  # Updated to use app.main module
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )