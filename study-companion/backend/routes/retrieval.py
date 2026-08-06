from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.qdrant_service import search_vectors
from services.embedding_service import model as embedding_model

router = APIRouter(
    tags=["Retrieval"]
)


class RetrievalRequest(BaseModel):
    query: str
    limit: int = 3


@router.post("/retrieve")
def retrieve(request: RetrievalRequest):
    """
    Embed the incoming text query (using the same model used to embed
    stored chunks) and retrieve the most relevant document chunks
    from the Qdrant vector database.
    """

    if not request.query or not request.query.strip():
        raise HTTPException(
            status_code=400,
            detail="Query text cannot be empty."
        )

    try:
        query_vector = embedding_model.encode(
            [request.query]
        )[0].tolist()

        results = search_vectors(
            query_vector=query_vector,
            limit=request.limit
        )

        return {
            "message": "Retrieval successful.",
            "results": results
        }

    except Exception as e:
        print(f"Retrieval error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Retrieval failed: {str(e)}"
        )