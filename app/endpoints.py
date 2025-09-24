from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import URLCreate, URLResponse
from app.database import get_db_session
from app.storage import (
    generate_short_code,
    store_url_mapping,
    get_original_url,
    increment_click_count,
    get_url_info
)
from app.database import URLMapping
from sqlalchemy import select
from typing import List

# Create APIRouter instance for endpoints
router = APIRouter()

@router.post("/shorten", response_model=URLResponse)
async def shorten_url(
    url_data: URLCreate, 
    db: AsyncSession = Depends(get_db_session)
):
    
    # Extract the original URL from the request
    original_url = str(url_data.url)
    
    # Generate a unique short code (now checks database for uniqueness)
    short_code = await generate_short_code(db)
    
    # Store the URL mapping in the database
    await store_url_mapping(db, short_code, original_url)
    
    # Create the response with the short URL
    short_url = f"http://localhost:8000/{short_code}"
    
    return URLResponse(
        original_url=original_url,
        short_code=short_code,
        short_url=short_url
    )

@router.get("/{short_code}")
async def redirect_to_original(
    short_code: str, 
    db: AsyncSession = Depends(get_db_session)
):
   
    # Look up the original URL using the short code from database
    original_url = await get_original_url(db, short_code)
    
    # Check if the short code exists
    if original_url is None:
        raise HTTPException(
            status_code=404, 
            detail=f"Short code '{short_code}' not found"
        )
    
    # Increment the click count for analytics in database
    await increment_click_count(db, short_code)
    
    # Issue a redirect to the original URL
    return RedirectResponse(url=original_url, status_code=302)

