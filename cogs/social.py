import discord
from discord.ext import commands
import data_handler as dh

class Social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, member: discord.Member = None):
        """View your own or someone else's profile"""
        member = member or ctx.author
        user_id = str(member.id)
        user_data = dh.get_user(user_id)

        bio = "No bio set. Use `sm setbio`!" if not user_data["bio"] else user_data["bio"]
        balance = user_data["balance"]

        embed = discord.Embed(
            title=f"{member.display_name}'s Profile",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="💰 Balance", value=f"{balance} coins", inline=True)
        embed.add_field(name="📝 Bio", value=bio, inline=False)
        embed.set_footer(text=f"ID: {user_id}")

        await ctx.send(embed=embed)

    @commands.command()
    async def setbio(self, ctx, *, new_bio: str):
        """Update your profile bio"""
        if len(new_bio) > 100:
            return await ctx.send("Keep your bio under 100 characters!")

        user_id = str(ctx.author.id)
        user_data = dh.get_user(user_id)
        
        user_data["bio"] = new_bio
        dh.save_user(user_id, user_data)
        await ctx.send("✅ Bio updated!")

async def setup(bot):
    await bot.add_cog(Social(bot))
