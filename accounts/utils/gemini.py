from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

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

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
    )

    return response.text
