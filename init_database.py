"""
Database Initialization Script for Profit Flex Bot
Creates all necessary tables in PostgreSQL
"""

import logging
from sqlalchemy import text
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment
load_dotenv()

# Import database models
from models import engine, metadata, trade_logs, users, posts, success_stories

def init_database():
    """Initialize the database with all tables"""
    try:
        logger.info("Starting database initialization...")
        
        # Create all tables
        metadata.create_all(engine)
        logger.info("✅ All database tables created successfully!")
        
        # Verify tables exist
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT table_name FROM information_schema.tables 
                WHERE table_schema = 'public'
            """))
            tables = [row[0] for row in result]
            logger.info(f"📋 Existing tables: {', '.join(tables)}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {e}")
        raise

if __name__ == "__main__":
    init_database()
    logger.info("✅ Database setup complete!")
