# python-time

from discord.ext import commands
from datetime import datetime
from zoneinfo import ZoneInfo

class TimeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='시간')
    async def get_time(self, ctx):
        now = datetime.now(ZoneInfo("Asia/Seoul"))
        formatted_time = now.strftime("%p %I시 %M분")
        formatted_time = formatted_time.replace("AM", "오전").replace("PM", "오후")
        await ctx.send(f"지금은 {formatted_time} 일려나?")