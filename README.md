# Retrieval-Augmented Generation System

This project implements a Retrieval-Augmented Generation (RAG) system using free, locally runnable components.

---

## 📄 Document Source

- **File Used:** English_bulldog_genetics.pdf  
- **Extracted File:** `Selected_Document.txt`

---

## 🧠 RAG System Structure

- **Embedding Model:** `sentence-transformers/all-distilroberta-v1`
- **Chunk Size:** 500 characters
- **Chunk Overlap:** 50 characters
- **Text Splitter:** RecursiveCharacterTextSplitter
- **Vector Store:** FAISS IndexFlatL2
- **Text Generator:** HuggingFace FLAN-T5 Small

---

## 🔍 Retrieval Observations

### 1. Chunk Size & Overlap Testing
| Chunk Size | Chunk Overlap | Retrieval Quality |
|------------|----------------|--------------------|
| 300        | 50             | More specific results, occasionally incomplete context |
| 500        | 50             | Balanced results, best overall |
| 700        | 70             | Broader context but more latency |

📝 **Conclusion:** `chunk_size=500` and `chunk_overlap=50` offered the best trade-off.

---

## 🔎 Deep-Dive Questions and Answers

### Q1: What is the dimension of the sentence-transformers embedding?
A: `768` for `all-distilroberta-v1`.

### Q2: How does FAISS determine "similarity"?
A: FAISS uses L2 (Euclidean) distance between embedding vectors by default with `IndexFlatL2`.

### Q3: Why do we use chunk overlap?
A: To ensure continuity between segments; it reduces context fragmentation.

### Q4: Why do we split text by newlines and spaces?
A: It preserves paragraph integrity and natural boundaries between ideas.

### Q5: How is the prompt constructed?
A: As `"Context:\n{chunked context}\n\nQuestion: {question}\nAnswer:"`

---

## ✅ Summary

This RAG system successfully:
- Loaded a document
- Embedded it using Sentence-Transformers
- Indexed with FAISS
- Retrieved and answered questions using HuggingFace models

---

_Last updated: May 31, 2025_
