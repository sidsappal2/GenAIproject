# Python GenAI QA System with Streamlit UI

A question answering system using LangChain, Google's Generative AI, and Streamlit UI.

## Features

- Streamlit web interface
- Text chunking for processing large documents
- Embeddings generation using HuggingFace
- Vector storage using FAISS
- Integration with Google's Generative AI

## Prerequisites

- Python 3.8+
- Google API Key for Generative AI

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Create a `.env` file:
```env
GOOGLE_API_KEY="your_google_api_key_here"
```

## Usage

Start the Streamlit app:
```bash
streamlit run app.py
```

1. Paste your text in the text area
2. Click "Process Text" to analyze it
3. Enter your question
4. Click "Get Answer" to see the response

## Project Structure

```
├── app.py           # Streamlit UI
├── config.py        # Configuration settings
├── embeddings.py    # HuggingFace embeddings
├── llm.py          # Google Gen AI integration
├── qa_chain.py     # Question answering chain
├── text_splitter.py # Text chunking
├── vectorstore.py  # Vector store (FAISS)
├── requirements.txt # Dependencies
└── README.md       # Documentation
```