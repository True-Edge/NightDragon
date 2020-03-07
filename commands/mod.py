import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role("Staff")
    async def kick(self, ctx, member: discord.Member, *, reason="None"):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} Was Kicked By {ctx.author.mention}. [{reason}]")

    @commands.command()
    @commands.has_role("Staff")
    async def ban(self, ctx, member: discord.Member, *, reason="None"):
        await member.ban(reason=reason)    
        await ctx.channel.send(f"{member.mention} Was Banned By {ctx.author.mention}. [{reason}]")

    @commands.command(aliases=["purge"])
    @commands.has_role("Staff")
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{amount} Message Has Been Deleted")

def setup(bot):
    bot.add_cog(Mod(bot))
    print("\nMod.py Loaded\n")