import discord
from discord.ext import commands
import data_handler as dh
from datetime import date

class Economy(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
        """Claim your daily reward"""
        user_id = str(ctx.author.id)
        user_data = dh.get_user(user_id)
        today = str(date.today())

        if user_data["last_daily"] == today:
            await ctx.send("You've already claimed your daily reward today!")
            return

        reward = 100

        user_data["balance"] += reward
        user_data["daily_streak"] += 1
        user_data["last_daily"] = today
        
        dh.save_user(user_id, user_data)
        await ctx.send(f"Success! You claimed **{reward}** coins. New balance: {user_data['balance']}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Economy(bot))
