# utils/gemini_wrapper.py
import google.generativeai as genai
from config.settings import GEMINI_API_KEY

# Gemini API 초기화
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemma-3-27b-it")

def ask_gemini_question(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"오류 발생: {e}"
