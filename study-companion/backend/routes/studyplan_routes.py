from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.qdrant_service import search_vectors
from services.embedding_service import model as embedding_model
from services.study_plan_service import generate_study_plan

router = APIRouter(tags=["Study Plan"])


class StudyPlanRequest(BaseModel):
    goal: str
    current_skills: str = ""
    available_time: str = ""
    duration: str = ""
    limit: int = 5


@router.post("/study-plan")
def create_study_plan(request: StudyPlanRequest):
    """
    Retrieve relevant chunks from Qdrant based on the goal/topic,
    then generate a study plan using Gemini.
    """
    if not request.goal or not request.goal.strip():
        raise HTTPException(status_code=400, detail="Goal cannot be empty.")

    try:
        query_vector = embedding_model.encode([request.goal])[0].tolist()
        retrieved_chunks = search_vectors(query_vector=query_vector, limit=request.limit)

        result = generate_study_plan(
            goal=request.goal,
            current_skills=request.current_skills,
            available_time=request.available_time,
            duration=request.duration,
            retrieved_chunks=retrieved_chunks
        )

        if result.get("status") == "error":
            raise HTTPException(
                status_code=500,
                detail=result.get("message", "Study plan generation failed.")
            )

        return result

    except HTTPException:
        raise
    except Exception as e:
        print(f"Study plan error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Study plan generation failed: {str(e)}"
        )