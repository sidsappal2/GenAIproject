"""Vector store implementation."""

from langchain.vectorstores import FAISS
from langchain.embeddings.base import Embeddings

def create_vectorstore(texts: list[str], embeddings: Embeddings):
    """Create a vector store from text chunks.
    
    Args:
        texts: List of text chunks
        embeddings: Embeddings instance
        
    Returns:
        Initialized vector store
    """
    return FAISS.from_texts(texts, embeddings)