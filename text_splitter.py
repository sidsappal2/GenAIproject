"""Text splitting functionality."""

from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import Config

def split_text(text: str) -> list[str]:
    """Split text into manageable chunks.
    
    Args:
        text: Input text to split
        
    Returns:
        List of text chunks
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP
    )
    return splitter.split_text(text)