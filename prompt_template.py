def build_resume_comparison_prompt(resume_text, job_description):
    return f"""
You are an AI resume screening assistant.

Compare the resume with the job description and return only valid JSON
with exactly this structure:

{{
  "match_score": 0,
  "missing_keywords": [],
  "suggestions": []
}}

Rules:
- match_score must be an integer from 0 to 100.
- missing_keywords must be a list of strings.
- suggestions must be a list of clear resume rewrite suggestions.
- Do not include Markdown, code fences, or text outside the JSON.

Resume:
{resume_text}

Job description:
{job_description}
""".strip()