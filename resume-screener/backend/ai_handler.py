import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError

from prompt_template import build_resume_comparison_prompt

load_dotenv()


def screen_resume(resume_text, job_description):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing from the .env file.")

    prompt = build_resume_comparison_prompt(
        resume_text,
        job_description
    )

    client = genai.Client(api_key=api_key)

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                ),
            )

            return response.text

        except ServerError:

            if attempt < 2:

                print("Gemini busy... retrying...")
                time.sleep(3)

            else:

                raise Exception(
                    "Gemini servers are temporarily busy. Please try again in a few minutes."
                )