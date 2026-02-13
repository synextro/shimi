import discord
from discord.ext import commands
import random
import asyncio
import data_handler as dh

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def guess(self, ctx: commands.Context):
        number = random.randint(1, 10)
        attemps = 3

        await ctx.send("guess the number from 1 to 10")

        def check(m: discord.Message):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

        for i in range(attemps):
            try:
                msg = await self.bot.wait_for('message', check=check, timeout=20.0)
                guess = int(msg.content)

                if guess > number:
                    await ctx.send("lower")
                elif guess > number:
                    await ctx.send("higher")
                else:
                    user_id = str(ctx.author.id)
                    user_data = dh.get_user(user_id)

                    user_data["balance"] += 50

                    dh.save_user(user_id, user_data)

                    return await ctx.send(f"Correct! You won **50 coins**")
            except asyncio.TimeoutError:
                return await ctx.send(f"time is up, the number is {number}")
        
        await ctx.send(f"out of tries, the number is {number}")

async def setup(bot):
    await bot.add_cog(Fun(bot))
