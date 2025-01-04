"""HuggingFace embeddings configuration."""

from langchain.embeddings import HuggingFaceEmbeddings

def create_embeddings():
    """Create and configure HuggingFace embeddings.
    
    Returns:
        Configured embeddings instance
    """
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )