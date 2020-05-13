import discord
from discord.ext import commands

class VerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def version(self, ctx):
        embed = discord.Embed(title="Bot Addition Info", color=discord.Color.from_rgb(255, 215, 0))
        embed.add_field(name="Version", value="1.4")
        embed.add_field(name="Release Version", value="[Stable]")
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(VerCog(bot))