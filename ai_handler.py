import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompt_template import build_resume_comparison_prompt


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

    # Validation and conversion into the final structure will be handled separately.
    return response.text