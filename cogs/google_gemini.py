# google-gemini

from discord.ext import commands
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='질문')
    async def ask_gemini(self, ctx, *, question):
        try:
            thinking_msg = await ctx.send(f"'{question}' 에 대해 생각 해볼려구... 잠시 기다려봐")

            model = genai.GenerativeModel("gemma-3-27b-it")
            response = model.generate_content(question)

            await ctx.send(response.text[:1900])
        except Exception as e:
            await ctx.send(f"오류 발생: {e}")