**RAG-Based Question Answering System**
This project implements a Retrieval-Augmented Generation (RAG) system using Google Gemini and ChromaDB with embeddings from HuggingFace. It allows users to ask questions and get informative answers based on provided document content.
Features
<H4>PDF Document Ingestion:</H4> Extracts and processes content from PDF files.
<H4>Text Chunking: </H4>Splits large documents into smaller, manageable chunks using RecursiveCharacterTextSplitter.
<H4>Embedding Generation: </H4>Uses HuggingFace's all-MiniLM-L6-v2 for generating embeddings.
<H4>Contextual Search:</H4> Stores and queries vector embeddings using ChromaDB.
<H4>Answer Generation:</H4> Leverages Google Gemini API (Generative AI) to provide human-friendly answers.

<H2>Requirements</H2>
<H4>Ensure you have the following dependencies installed:</H4>

Python 3.8+
Required Libraries
pip install google-generativeai langchain langchain-community chromadb sentence-transformers pypdf

**How It Works
Load PDF Document:** The project uses PyPDFLoader to read and extract text from PDF files.
**Split Text: **The text is split into smaller chunks using RecursiveCharacterTextSplitter.
**Generate Embeddings:** HuggingFace's all-MiniLM-L6-v2 creates embeddings for each chunk.
**Store in ChromaDB:** Chunks and their embeddings are stored in a persistent ChromaDB.
**Retrieve Context:** The system retrieves the top K relevant text chunks based on a query.
**Generate Answer:** Google Gemini generates an answer based on the question and retrieved context.
