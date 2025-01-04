"""Question answering chain implementation."""

from langchain.vectorstores.base import VectorStore
from llm import create_llm

def create_qa_chain(vectorstore: VectorStore):
    """Create a question answering chain.
    
    Args:
        vectorstore: Initialized vector store
        
    Returns:
        Question answering function
    """
    llm = create_llm()
    
    async def qa_chain(question: str) -> str:
        relevant_docs = vectorstore.similarity_search(question, k=3)
        context = "\n\n".join(doc.page_content for doc in relevant_docs)
        
        prompt = f"""
        Context: {context}
        
        Question: {question}
        
        Please answer the question based on the context provided. If you cannot find the answer in the context, say "I cannot answer this question based on the provided context."
        
        Answer:"""
        
        response = llm.generate_content(prompt)
        return response.text
        
    return qa_chain