<h1>RAG-Based Question Answering System</h1>
This project implements a Retrieval-Augmented Generation (RAG) system using Google Gemini and ChromaDB with embeddings from HuggingFace. It allows users to ask questions and get informative answers based on provided document content.
Features
<H4>PDF Document Ingestion:</H4> Extracts and processes content from PDF files.
<H4>Text Chunking: </H4>Splits large documents into smaller, manageable chunks using RecursiveCharacterTextSplitter.
<H4>Embedding Generation: </H4>Uses HuggingFace's all-MiniLM-L6-v2 for generating embeddings.
<H4>Contextual Search:</H4> Stores and queries vector embeddings using ChromaDB.
<H4>Answer Generation:</H4> Leverages Google Gemini API (Generative AI) to provide human-friendly answers.
<h2>Output:</h2>
![image](https://github.com/user-attachments/assets/a2ace8bd-da33-4bca-aef3-dd9cedb9f142)

<br>
![image](https://github.com/user-attachments/assets/7f4a45d5-68fe-4655-aaba-99888338930d)

<H2>Requirements</H2>
<H4>Ensure you have the following dependencies installed:</H4>
<br>
Python 3.8+<br>
Required Libraries<br>
<u>pip install google-generativeai langchain langchain-community chromadb sentence-transformers pypdf</u>
<br>
<h4>How It Works </h4></br>
<h5>Load PDF Document:</h5> The project uses PyPDFLoader to read and extract text from PDF files.<br>
<h5>Split Text: </h5>The text is split into smaller chunks using RecursiveCharacterTextSplitter.<br>
<h5>Generate Embeddings:</h5> HuggingFace's all-MiniLM-L6-v2 creates embeddings for each chunk.<br>
<h5>Store in ChromaDB:</h5> Chunks and their embeddings are stored in a persistent ChromaDB.<br>
<h5>Retrieve Context:</h5> The system retrieves the top K relevant text chunks based on a query.<br>
<h5>Generate Answer:</h5> Google Gemini generates an answer based on the question and retrieved context.<br>
