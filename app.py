"""Streamlit UI for GenAI QA system."""

import streamlit as st
from text_splitter import split_text
from embeddings import create_embeddings
from vectorstore import create_vectorstore
from qa_chain import create_qa_chain

st.set_page_config(page_title="GenAI QA System", page_icon="🤖")

st.title("GenAI Question Answering System")

# Text input area
text_input = st.text_area(
    "Paste your text here:",
    height=300,
    placeholder="Enter the text you want to analyze..."
)

# Question input
question = st.text_input("Ask a question about the text:", placeholder="Enter your question...")

# Initialize session state
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

# Process text button
if st.button("Process Text"):
    with st.spinner("Processing text..."):
        # Split text into chunks
        chunks = split_text(text_input)
        
        # Create embeddings
        embeddings = create_embeddings()
        
        # Create vector store
        vectorstore = create_vectorstore(chunks, embeddings)
        
        # Create QA chain
        st.session_state.qa_chain = create_qa_chain(vectorstore)
        
        st.success("Text processed successfully!")

# Answer question button
if st.button("Get Answer") and question and st.session_state.qa_chain:
    with st.spinner("Finding answer..."):
        answer = st.session_state.qa_chain(question)
        st.write("### Answer:")
        st.write(answer)
elif st.button("Get Answer") and not st.session_state.qa_chain:
    st.warning("Please process the text first before asking questions.")