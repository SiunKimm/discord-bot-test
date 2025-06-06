# utils/gemini_wrapper.py
import asyncio
import google.generativeai as genai
from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemma-3-27b-it")

async def ask_gemini_question(prompt: str) -> str:
    loop = asyncio.get_running_loop()
    try:
        response = await asyncio.wait_for(
            loop.run_in_executor(None, model.generate_content, prompt),
            timeout=30
        )
        return getattr(response, "text", "Gemini 응답 없음")
    except asyncio.TimeoutError:
        return "Gemini 응답 시간이 너무 오래 걸려 타임아웃이 발생했어요."
    except Exception as e:
        return f"Gemini 응답 중 오류 발생: {e}"
