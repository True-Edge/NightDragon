import discord
from discord.ext import commands

class VerCog(commands.Cog):
    def __init__(self, client):
        self.bot = bot

    @commands.command()
    async def version(self, ctx):
        await ctx.send("Version 1.2.0 [Near Stable]")
        
def setup(bot):
    bot.add_cog(VerCog(bot))