from fastapi import FastAPI
from routes.retrieval import router

app = FastAPI(
    title="AI Study Companion",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Study Companion Backend Running"}