# bot.py
import os
import discord
from discord.ext import commands
from discord import app_commands

from cogs.user_analysis import UserAnalysisCog

from config.settings import DISCORD_TOKEN

# 디스코드 봇 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True

# 봇 인스턴스 생성
bot = commands.Bot(command_prefix="/", intents=intents)

# 봇이 준비되었을 때 실행되는 이벤트
@bot.event
async def on_ready():
    print(f"봇 로그인 성공: {bot.user}")

# 슬래시 커맨드 등록 및 Cog 추가
@bot.event
async def setup_hook():
    # 모든 글로벌 커맨드 초기화
    bot.tree.clear_commands(guild=None)

    from cogs.python_dice import DiceCog
    from cogs.python_time import TimeCog
    from cogs.google_gemini import GeminiCog
    from cogs.user_analysis import UserAnalysisCog

    await bot.add_cog(DiceCog(bot))
    await bot.add_cog(TimeCog(bot))
    await bot.add_cog(GeminiCog(bot))
    await bot.add_cog(UserAnalysisCog(bot))

    # 글로벌 커맨드 재등록
    await bot.tree.sync()
    print("✅ 커맨드 초기화 및 재등록 완료")

# 봇 실행
bot.run(DISCORD_TOKEN)
