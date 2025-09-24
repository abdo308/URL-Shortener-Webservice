from pydantic import BaseModel, HttpUrl
from typing import Dict, Any
from datetime import datetime

# Pydantic Models for API requests and responses

class URLCreate(BaseModel):
    """Model for the request to shorten a URL"""
    url: HttpUrl  # This validates that the input is a proper URL

class URLResponse(BaseModel):
    """Model for the response after shortening a URL"""
    original_url: str
    short_code: str
    short_url: str

# In-memory storage for our URL mappings
# In production, this would be replaced with a database
url_database: Dict[str, Any] = {}

# Structure of each entry in url_database:
# {
#     "short_code": {
#         "original_url": "https://example.com",
#         "created_at": datetime object,
#         "click_count": integer
#     }
# }