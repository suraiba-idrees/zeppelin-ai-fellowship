import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Please add it to your .env file.")

client = genai.Client(api_key=GEMINI_API_KEY)

def build_study_plan_prompt(
    goal: str,
    current_skills: str,
    available_time: str,
    duration: str,
    retrieved_chunks: list[str]
):
    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are an expert AI study planner.

Create a personalized study plan using the user's goals and the retrieved syllabus information.

User Information:

Learning Goal:
{goal}

Current Skills:
{current_skills}

Available Time:
{available_time}

Study Duration:
{duration}


Retrieved Syllabus Content:
{context}


Generate:

1. Learning roadmap
2. Weekly study schedule
3. Topics to cover
4. Practical exercises/projects
5. Revision strategy
6. Recommended resources

Make the plan realistic, structured, and easy to follow.
"""

    return prompt

def generate_study_plan(
    goal: str,
    current_skills: str,
    available_time: str,
    duration: str,
    retrieved_chunks: list[str]
):
    """
    Generates a personalized study plan using Gemini AI.

    Parameters:
        goal: User's learning goal
        current_skills: Existing skills/background
        available_time: Hours available per day/week
        duration: Desired learning duration

    Returns:
        Generated study plan text
    """

prompt = build_study_plan_prompt(
    goal,
    current_skills,
    available_time,
    duration,
    retrieved_chunks
)


try:
        response = client.models.generate_content(
    model="gemini-2.0-flash-lite",
    contents=prompt
)

        return {
    "status": "success",
    "study_plan": response.text
}

except Exception as e:
        return {
    "status": "error",
    "message": str(e)
}


# Test function (temporary)
