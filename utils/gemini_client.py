import os
from google import genai
from dotenv import load_dotenv
from config import GEMINI_MODEL

# Load .env file
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please set environment variable.")

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt):

    try:

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"⚠ Gemini API Error: {str(e)}"