from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

#load pdf
loaders = [PyPDFLoader('./r.pdf')]

docs = []

for file in loaders:
    docs.extend(file.load())

#split 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(docs)

#vector embeddings
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'})

#store in chromadb
vectorstore = Chroma.from_documents(docs, embedding_function, persist_directory="./chroma_db_nccn")

print(vectorstore._collection.count())