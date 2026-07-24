from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.analysis import router

app = FastAPI(
    title="AI Resume Screener",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api", tags=["Analysis"])

@app.get("/")
def home():
    return {
        "message": "AI Resume Screener Backend Running"
    }
if __name__ == "__main__":
    import asyncio
    from fastapi.cli import main
    import sys
    # Yeh code direct fastapi developer runtime utility ko automatically trigger kar dega
    sys.argv = ["fastapi", "dev", "server.py"]
    try:
        main()
    except SystemExit:
        pass


