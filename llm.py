"""Google Generative AI integration."""

import google.generativeai as genai
from config import Config

def create_llm():
    """Create and configure Google's Generative AI model.
    
    Returns:
        Configured GenerativeAI model instance
    """
    genai.configure(api_key=Config.GOOGLE_API_KEY)
    return genai.GenerativeModel(Config.MODEL_NAME)