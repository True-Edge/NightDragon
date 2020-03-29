import discord
from discord.ext import commands

class DMSCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role("Staff")
    async def dm(self, ctx, member: discord.Member, reason="None"):
        await member.send(reason)
        await ctx.send("Message Sended")

def setup(bot):
    bot.add_cog(DMSCog(bot))