from google import genai
from google.genai.errors import ClientError

client = genai.Client(api_key="AIzaSyDNfkWOXh7RuSrhM4IhNswtukgZvLwLP4A")


def parse_resume_text(text):
    prompt = f"""
You are an ATS resume parser.

Extract structured JSON only:
{{
  "name": "",
  "email": "",
  "phone": "",
  "skills": [],
  "experience": [],
  "education": [],
  "summary": ""
}}

Resume Text:
{text}

Return ONLY valid JSON.
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",

            contents=prompt,
        )
        return response.text
    except ClientError as e:
        try:
            available = client.list_models()
        except Exception:
            available = None
        msg = (
            f"Model error: {e}.\nAvailable models: {available}"
        )
        raise RuntimeError(msg) from e
