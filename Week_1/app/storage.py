import string
import random
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.database import URLMapping

async def generate_short_code(session: AsyncSession, length: int = 6) -> str:
    """
    Generate a random short code of specified length.
    Uses letters (both cases) and digits.
    Ensures the generated code is unique by checking the database.
    """
    characters = string.ascii_letters + string.digits
    
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(length))
        
        # Check if this code already exists in the database
        result = await session.execute(
            select(URLMapping).where(URLMapping.short_code == short_code)
        )
        existing = result.scalar_one_or_none()
        
        if existing is None:  # Code doesn't exist, it's unique
            return short_code

async def store_url_mapping(session: AsyncSession, short_code: str, original_url: str) -> None:
    """
    Store the mapping between short code and original URL in the database.
    Also stores metadata like creation time and click count.
    """
    url_mapping = URLMapping(
        short_code=short_code,
        original_url=original_url,
        click_count=0
    )
    
    session.add(url_mapping)
    await session.commit()

async def get_original_url(session: AsyncSession, short_code: str) -> Optional[str]:
    """
    Retrieve the original URL for a given short code from the database.
    Returns None if the short code doesn't exist.
    """
    result = await session.execute(
        select(URLMapping).where(URLMapping.short_code == short_code)
    )
    url_mapping = result.scalar_one_or_none()
    
    if url_mapping:
        return url_mapping.original_url
    return None

async def increment_click_count(session: AsyncSession, short_code: str) -> None:
    """
    Increment the click count for a short code in the database.
    Used for tracking how many times a link has been accessed.
    """
    await session.execute(
        update(URLMapping)
        .where(URLMapping.short_code == short_code)
        .values(click_count=URLMapping.click_count + 1)
    )
    await session.commit()

async def get_url_info(session: AsyncSession, short_code: str) -> Optional[URLMapping]:
    """
    Get complete information about a short code from the database.
    Returns None if the short code doesn't exist.
    """
    result = await session.execute(
        select(URLMapping).where(URLMapping.short_code == short_code)
    )
    return result.scalar_one_or_none()