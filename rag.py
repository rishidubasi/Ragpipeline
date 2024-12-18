import os
import signal
import sys
import tkinter as tk
from tkinter import filedialog
import pdfplumber 

import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

GEMEINI_API_KEY = "AIzaSyCJVM38NOcxJ7hT9WO2IgmlgXa2zP1pS2U"

def signal_handler(sig, frame):
    print('\nThanks for using me. :)')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def extract_text_from_pdf(pdf_path):
    """Extract text from the uploaded PDF."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def upload_pdf():
    """Open a file dialog to upload a PDF."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    pdf_path = filedialog.askopenfilename(
        title="Select PDF File", 
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    return pdf_path

def generate_rag_prompt(query, context):
    """Generate the prompt for the RAG model."""
    escaped = context.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = ("""
You are a helpful and informative bot that answers questions using text from the reference context included below. \
Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
strike a friendly and conversational tone. \
If the context is irrelevant to the answer, you may ignore it.
    QUESTION: '{query}'
    CONTEXT: '{context}'
    ANSWER:
    """).format(query=query, context=context)
    return prompt

def get_relevant_context_from_db(query):
    """Fetch relevant context from the vector database."""
    context = ""
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = Chroma(persist_directory="./chroma_db_nccn", embedding_function=embedding_function)
    search_results = vector_db.similarity_search(query, k=6)
    for result in search_results:
        context += result.page_content + "\n"
    return context

def generate_answer(prompt):
    """Generate the answer using Google Generative AI."""
    genai.configure(api_key=GEMEINI_API_KEY)
    model = genai.GenerativeModel(model_name='gemini-pro')
    answer = model.generate_content(prompt)
    return answer.text

# Upload PDF and extract text
print("Please upload a PDF file.")
pdf_path = upload_pdf()
if not pdf_path:
    print("No PDF selected. Exiting.")
    sys.exit(1)

pdf_text = extract_text_from_pdf(pdf_path)
print("PDF uploaded and text extracted successfully.")

# Welcome message
welcome_text = generate_answer("Can you quickly introduce yourself")
print(welcome_text)

#
while True:
    print("-----------------------------------------------------------------------\n")
    print("What would you like to ask?")
    query = input("Query: ").strip()

    if not query:
        print("Please enter a valid query.")
        continue

 
    context_from_db = get_relevant_context_from_db(query)
    combined_context = pdf_text + "\n" + context_from_db
    prompt = generate_rag_prompt(query=query, context=combined_context)

    # Generate and display the answer
    answer = generate_answer(prompt=prompt)
    print("\nAnswer:", answer)
    print("\n-----------------------------------------------------------------------")
