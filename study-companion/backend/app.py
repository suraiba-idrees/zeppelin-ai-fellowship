from fastapi import FastAPI
from routes.document_routes import router as document_router
from routes.retrieval import router as retrieval_router
from services.qdrant_service import create_collection

app = FastAPI(
    title="AI Study Companion API",
    version="1.0.0"
)

app.include_router(document_router)
app.include_router(retrieval_router)

# Once Aniqa's study-plan route is ready, add:
# from routes.studyplan_routes import router as studyplan_router
# app.include_router(studyplan_router)


@app.on_event("startup")
def startup_event():
    # Make sure the Qdrant collection exists before the app starts serving requests
    create_collection()


@app.get("/")
async def root():
    return {
        "message": "AI Study Companion Backend is running."
    }