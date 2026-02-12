import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Shimi(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=["sm ", "sm"],
            intents=discord.Intents.all(),
            status=discord.Status.idle,
        )

    async def setup_hook(self):
        await self.load_extension("cogs.economy")
        print("economy cog loaded")

bot = Shimi()

@bot.event
async def on_ready():
    assert bot.user is not None
    print(f"Logged in as {bot.user.display_name} (ID: {bot.user.id})")

@bot.command()
async def ping(ctx: commands.Context):
    """Get the bot's latency"""
    await ctx.send(f"pong! {bot.latency * 1000:.2f}ms")

token = os.getenv("TOKEN")
if not token:
    raise ValueError("TOKEN not found in .env file")

bot.run(token)
