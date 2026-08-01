from fastapi import FastAPI
from routes.document_routes import router

app = FastAPI(
    title="AI Study Companion API",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {
        "message": "AI Study Companion Backend is running."
    }

