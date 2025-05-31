# prompts.md

This document lists all the AI prompts used to generate code and configuration for the RAG system.

---

## 🔹 Setup and Requirements

**Prompt:**  
"Write the pip install commands needed for:  
beautifulsoup4, langchain, sentence-transformers, numpy, faiss-cpu, transformers, torch"

**Prompt:**  
"Generate a requirements.txt listing exactly those seven libraries (one per line)."

---

## 🔹 PDF Extractor

**Prompt:**  
"Write a Python function called `extract_text_from_pdf(pdf_path)` that opens a PDF file named [insert your PDF filename] at [insert your PDF path] (using PyPDF2 or pdfminer.six), iterates through every page to extract its text, collapses extra whitespace, writes the combined text to `Selected_Document.txt` (UTF‑8), prints a success/failure message if the file can’t be opened or read, and returns the full document text. Also include a `main()` function and an `if __name__ == '__main__':` block."

---

## 🔹 Web Scraper

**Prompt:**  
"Write a Python function called `scrape_webpage(url)` that uses requests to fetch [insert the URL you want to scrape], parses it with BeautifulSoup, extracts all <p> tags inside <div class='mw-parser-output'>, joins their text with blank lines, writes the result to Selected_Document.txt (UTF‑8), prints a success/failure message based on the HTTP status code, and returns the article text. Please hard‑code the URL in the function. Also include a main() function and an `if __name__ == '__main__':` block."

---

## 🔹 RAG Embedding & Retrieval Pipeline

**Prompt:**  
"Write code to import logging, transformers.logging (as hf_logging), and warnings; then set the log level of langchain.text_splitter and transformers to ERROR, and filter Python warnings."

**Prompt:**  
"Write code to define the variables:  
chunk_size = 500  
chunk_overlap = 50  
model_name = 'sentence-transformers/all-distilroberta-v1'  
top_k = 5"

**Prompt:**  
"Write code to open Selected_Document.txt in UTF‑8 mode, read its contents into a variable text."

**Prompt:**  
"Write code to import and use RecursiveCharacterTextSplitter (with separators ['\n\n', '\n', ' ', '']) to split text into a list of chunks."

**Prompt:**  
"Write code to load SentenceTransformer(model_name), encode chunks (showing a hidden progress bar), convert the result to a NumPy float32 array, initialize a FAISS IndexFlatL2, add the array to it."

**Prompt:**  
"Write code to import and set up a HuggingFace pipeline('text2text-generation', model='google/flan-t5-small', device=-1)."

**Prompt:**  
"Write functions:  
- `retrieve_chunks(question, k=top_k)`  
- `answer_question(question)`"

**Prompt:**  
"Write code for an interactive loop so the user can keep asking questions until they type ‘exit’ or ‘quit’."
