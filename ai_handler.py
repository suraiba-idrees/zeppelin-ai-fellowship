import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

from prompt_template import build_resume_comparison_prompt

# Enforces types validation matching our frontend schema requirements
class AnalysisResponse(BaseModel):
    match_score: int = Field(..., ge=0, le=100)
    missing_keywords: List[str]
    suggestions: List[str]

# Load the Gemini API key from the local .env file.
load_dotenv()


def screen_resume(resume_text, job_description):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing from the .env file.")

    # Build the comparison prompt and send it to Gemini.
    prompt = build_resume_comparison_prompt(resume_text, job_description)
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        ),
    )

    raw_text = response.text.strip()

    # Validation and conversion step handling structure safely
    try:
        parsed_json = json.loads(raw_text)
        AnalysisResponse(**parsed_json) # Assures formatting health before backend delivery
        return raw_text
        
    except Exception as e:
        print(f"JSON Structure Validation error fallback: {e}")
        # Secure placeholder layout configuration if model breaks schema definitions
        return json.dumps({
            "match_score": 0,
            "missing_keywords": ["Validation processing failure across document layout."],
            "suggestions": ["Please verify the input format structures and try re-submitting profile parameters."]
        })
