# RAG_app.py

# Step 1: Suppress logging & warnings
import logging
import warnings
from transformers.utils.logging import get_logger

hf_logging = get_logger(__name__)
hf_logging.setLevel(logging.ERROR)

logging.getLogger("langchain.text_splitter").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")

# Step 2: Set parameters
chunk_size = 500
chunk_overlap = 50
model_name = "sentence-transformers/all-distilroberta-v1"
top_k = 5

# Step 3: Read cleaned document
with open("Selected_Document.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Step 4: Split into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=["\n\n", "\n", " ", ""]
)
chunks = splitter.split_text(text)
print(f"✅ Text split into {len(chunks)} chunks.")

# Step 5: Embed with SentenceTransformer & build FAISS index
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer(model_name)
embeddings = model.encode(chunks, show_progress_bar=True)
embedding_array = np.array(embeddings).astype("float32")

index = faiss.IndexFlatL2(embedding_array.shape[1])
index.add(embedding_array)
print("✅ FAISS index created.")

# Step 6: Load HuggingFace generation model
from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-small", device=-1)
print("✅ Generator loaded.")

# Step 7: Retrieval and answer functions
def retrieve_chunks(question, k=top_k):
    question_embedding = model.encode([question]).astype("float32")
    distances, indices = index.search(question_embedding, k)
    return [chunks[i] for i in indices[0]]

def answer_question(question):
    context = "\n\n".join(retrieve_chunks(question))
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    response = generator(prompt, max_length=200)
    return response[0]['generated_text']

# Step 8: Interactive loop
if __name__ == "__main__":
    print("✅ RAG system ready.")
    print("Type your question. Enter 'exit' or 'quit' to end.\n")

    while True:
        query = input("Your question: ")
        if query.lower() in ("exit", "quit"):
            break
        print("Answer:", answer_question(query))
        print("\n" + "-"*60 + "\n")
