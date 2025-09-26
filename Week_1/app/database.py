from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from datetime import datetime
import os

# Create the base class for our database models
Base = declarative_base()

class URLMapping(Base):
    """
    Database table to store URL mappings
    This replaces our in-memory dictionary
    """
    __tablename__ = "url_mappings"
    
    # Primary key: the short code (unique)
    short_code = Column(String(10), primary_key=True, index=True)
    
    # The original long URL
    original_url = Column(String(2000), nullable=False)
    
    # When this mapping was created
    created_at = Column(DateTime, default=datetime.now)
    
    # How many times this short code has been accessed
    click_count = Column(Integer, default=0)

# Database connection setup
DATABASE_PATH = os.getenv("DATABASE_PATH", "/app/data/url_shortener.db")
DATABASE_URL = f"sqlite+aiosqlite:///{DATABASE_PATH}"

# Create async engine for database operations
engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True shows SQL queries in logs

# Create session factory for database operations
AsyncSessionLocal = async_sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

async def create_tables():
    """
    Create all database tables
    This will create the url_mappings table if it doesn't exist
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db_session():
    """
    Dependency function to get database session
    This ensures proper session management
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()