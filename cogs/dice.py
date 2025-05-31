# dice.py

from discord.ext import commands
import random

class DiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='주사위')
    async def roll_dice(self, ctx):
        num = random.randint(1, 6)
        await ctx.send(f"주사위 결과: {num}")