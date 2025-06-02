# cogs/google_gemini.py
import discord
from discord import app_commands
from discord.ext import commands
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="질문", description="Gemini에게 질문을 합니다.")
    async def ask_gemini(self, interaction: discord.Interaction, question: str):
        await interaction.response.send_message(f"'{question}' 에 대해 생각 중... 잠시만 기다려줘!", ephemeral=True)

        try:
            model = genai.GenerativeModel("gemma-3-27b-it")
            response = model.generate_content(question)
            await interaction.followup.send(response.text[:1900])
        except Exception as e:
            await interaction.followup.send(f"오류 발생: {e}")