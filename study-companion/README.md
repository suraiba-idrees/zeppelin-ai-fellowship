# AI Study Companion

An AI-powered Study Companion developed as part of the **Zeppelin AI & Generative AI Fellowship – Week 3**.

The application is designed to help students study more efficiently by retrieving relevant information from uploaded study materials and generating structured study plans using Retrieval-Augmented Generation (RAG).

---

## Project Status

🚧 **Week 3 – In Development**

Current focus is building the Retrieval-Augmented Generation (RAG) pipeline.

---

## Week 3 Objectives

- Upload syllabus or study notes (PDF/TXT)
- Extract document text
- Split documents into meaningful chunks
- Generate embeddings
- Store embeddings in Qdrant Vector Database
- Retrieve relevant study content
- Generate a structured AI study plan

---

## Tech Stack

### Frontend
- Next.js

### Backend
- FastAPI

### Vector Database
- Qdrant

### LLM
- Google Gemini

---

## Project Structure

```
study-companion/
│
├── frontend/
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── utils/
│
└── README.md
```

---

## Current Progress

- ✅ Backend project structure
- ✅ Retrieval endpoint
- ✅ Qdrant integration
- 🚧 Document upload
- 🚧 Chunking
- 🚧 Embeddings
- 🚧 Study Plan Generation

---

## Week 3 Workflow

```
Upload Document
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
Retrieve Relevant Chunks
        │
        ▼
Generate AI Study Plan
```

---

## Contributors

| Team Member | Responsibility |
|------------|----------------|
| Saboora | Document Upload & Text Extraction |
| Maryam | Chunking & Embedding Generation |
| Suraiba Idrees | Qdrant Setup, Retrieval, Final Integration & README |
| Aniqa | Study Plan Generation (Gemini) |

---

## Upcoming (Week 4)

- Adaptive Quiz Generation
- Progress Tracking
- Learning History
- Personalized Recommendations

---

## License

Developed for educational purposes as part of the Zeppelin AI & Generative AI Fellowship.