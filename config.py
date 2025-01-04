"""Configuration settings for the GenAI QA system."""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class for the application."""
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    MODEL_NAME = "gemini-pro"
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200