<div align="center">

# 📚 AI Study Companion

### RAG-Powered Study Assistant — Zeppelin AI & Generative AI Fellowship (Week 3)

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-black?logo=next.js&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector%20Database-red)
![Gemini](https://img.shields.io/badge/Google%20Gemini-LLM-orange?logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Week%203-Complete-success)

</div>

---

## Overview

AI Study Companion helps students learn more efficiently by turning their own syllabus or notes into a searchable knowledge base. It uses **Retrieval-Augmented Generation (RAG)**: uploaded documents are chunked and embedded, stored in a vector database, and retrieved on demand to ground an LLM-generated study plan in the student's actual material — rather than generic, made-up advice.

---

## Week 3 Objectives

- [x] Upload syllabus or study notes (PDF/TXT)
- [x] Extract document text
- [x] Split documents into meaningful chunks
- [x] Generate embeddings
- [x] Store embeddings in a Qdrant vector database
- [x] Retrieve relevant study content for a given topic
- [x] Generate a structured AI study plan using retrieved content

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js |
| Backend | FastAPI |
| Vector Database | Qdrant |
| Embedding Model | `all-MiniLM-L6-v2` (Sentence Transformers) |
| LLM | Google Gemini |

---

## Project Structure

```
study-companion/
│
├── frontend/
│
├── backend/
│   ├── routes/
│   │   ├── document_routes.py     # Upload → chunk → embed → store
│   │   ├── retrieval.py           # Query → embed → search Qdrant
│   │   └── studyplan_routes.py    # Retrieve + generate plan via Gemini
│   ├── services/
│   │   ├── document_service.py    # PDF/TXT text extraction
│   │   ├── embedding_service.py   # Chunking + embedding generation
│   │   ├── qdrant_service.py      # Qdrant collection + vector search
│   │   ├── study_plan_service.py  # Gemini study plan generation
│   │   └── check_models.py        # Lists available Gemini models
│   ├── app.py                     # FastAPI entrypoint
│   └── requirements.txt
│
└── README.md
```

---

## How It Works

```
Upload Document (PDF/TXT)
        │
        ▼
Extract Text
        │
        ▼
Chunk Document
        │
        ▼
Generate Embeddings
        │
        ▼
Store in Qdrant
        │
        ▼
Retrieve Relevant Chunks (by topic/query)
        │
        ▼
Generate AI Study Plan (Gemini)
```

---

## Qdrant Setup

1. Run Qdrant locally via Docker:
   ```bash
   docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
   ```
2. Add to your `.env` file:
   ```
   QDRANT_URL=http://localhost:6333
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   If `QDRANT_URL` is not set, the app falls back to in-memory mode (data is lost on restart) — fine for quick testing, but use the Docker instance for a persistent collection.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the API (from `study-companion/backend`):
   ```bash
   uvicorn app:app --reload
   ```
5. The `study_notes` collection is created automatically on startup, with vector size auto-matched to the embedding model (384 dimensions, cosine distance).

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/documents/upload` | Upload a PDF/TXT file — extracts, chunks, embeds, and stores it in Qdrant |
| `POST` | `/retrieve` | Search stored chunks by topic/query |
| `POST` | `/study-plan` | Retrieve relevant chunks and generate a study plan via Gemini |

Full interactive docs available at `http://127.0.0.1:8000/docs` once the server is running.

---

## Contributors

| Team Member | Responsibility |
|---|---|
| Saboora | Document Upload & Text Extraction |
| Maryam | Chunking & Embedding Generation |
| Suraiba Idrees | Qdrant Setup, Retrieval, Final Integration & README |
| Aniqa | Study Plan Generation (Gemini) |

---

## Upcoming (Week 4)

- Adaptive quiz generation
- Progress tracking
- Learning history
- Personalized recommendations

---

## License

Developed for educational purposes as part of the Zeppelin AI & Generative AI Fellowship.