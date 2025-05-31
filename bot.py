# bot.py

import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"봇 로그인 성공: {bot.user}")

@bot.event
async def setup_hook():
    from cogs.python_dice import DiceCog
    await bot.add_cog(DiceCog(bot))
    from cogs.python_time import TimeCog
    await bot.add_cog(TimeCog(bot))
    from cogs.google_gemini import GeminiCog
    await bot.add_cog(GeminiCog(bot))

bot.run(TOKEN)
