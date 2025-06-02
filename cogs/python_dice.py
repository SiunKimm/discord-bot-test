# cogs/python_dice.py
import discord
from discord import app_commands
from discord.ext import commands
import random

class DiceCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="주사위", description="1부터 6까지의 주사위를 굴립니다.")
    async def roll_dice(self, interaction: discord.Interaction):
        num = random.randint(1, 6)
        await interaction.response.send_message(f"🎲 주사위 결과: {num}")