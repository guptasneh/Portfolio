import os
import logging
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime, timezone

# Load env variables from Backend/.env
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Fallback to local MongoDB if not provided
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = os.getenv('DB_NAME', 'cipherlab')

client = None

def get_db():
    global client
    if client is None:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    return client[DB_NAME]

def init_db():
    """
    Ensure the target database and collections exist/are accessible.
    """
    logger.info("Initializing database schema...")
    try:
        db = get_db()
        # Verify connection
        db.command('ping')
        logger.info("Connected to MongoDB successfully.")
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB at {MONGO_URI}. Is MongoDB running? Error: {e}")
        raise e

def insert_contact(name, email, subject, message):
    """
    Inserts a contact ticket into MongoDB.
    """
    db = get_db()
    try:
        db.contacts.insert_one({
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
            "created_at": datetime.now(timezone.utc)
        })
        return True
    except Exception as e:
        logger.error(f"Failed to insert contact message: {e}")
        raise e

def insert_feedback(rating, comments):
    """
    Inserts user feedback into MongoDB.
    """
    db = get_db()
    try:
        db.feedback.insert_one({
            "rating": rating,
            "comments": comments,
            "created_at": datetime.now(timezone.utc)
        })
        return True
    except Exception as e:
        logger.error(f"Failed to insert feedback: {e}")
        raise e
