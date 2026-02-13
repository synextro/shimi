import discord
from discord.ext import commands
import data_handler as dh
import datetime
import os
import json

class Economy(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
        data = dh.load_data()
        user_id = str(ctx.author.id)
        today = str(datetime.date.today())

        if user_id not in data:
            data[user_id] = { "balance": 0, "daily_streak": 0, "last_daily": None }

        if data[user_id]["last_daily"] == today:
            await ctx.send("You've already claimed your daily reward today!")
            return

        reward = 100
        data[user_id]["balance"] += reward
        data[user_id]["last_daily"] = today
        
        save_data(data)
        await ctx.send(f"Success! You claimed **{reward}** coins. New balance: {data[user_id]['balance']}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Economy(bot))
