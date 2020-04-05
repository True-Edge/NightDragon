import discord
import os
from discord.ext import commands
from discord.utils import get

pref = open("System/prefix.u.g", "r").read()
bot = commands.Bot(command_prefix = pref, case_insensitive=True)
class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role("Staff")
    async def kick(self, ctx, member: discord.Member, *, reason="None"):
        await member.kick(reason=reason)
        logs = get(ctx.guild.channels, name="logs")
        embed = discord.Embed(title="Member Kicked", colour=discord.Color.from_rgb(255, 215, 0))
        
        embed.add_field(name=f"{member} Was Kicked By -", value=ctx.author.mention)
        embed.add_field(name="Reason - ", value=reason)
        embed.set_footer(text=f"Kicked By Mod/Owner - {ctx.message.author}", icon_url=ctx.author.avatar_url)
        await member.send(embed=embed)
        await logs.send(embed=embed)

    @commands.command()
    @commands.has_role("Staff")
    async def ban(self, ctx, member: discord.Member, *, reason="None"):
        await member.ban(reason=reason)
        logs = get(ctx.guild.channels, name="logs")
        embed = discord.Embed(title="Member Banned", colour=discord.Color.from_rgb(255, 215, 0))

        embed.add_field(name=f"{member} Was Banned By - ", value=ctx.author.mention)
        embed.add_field(name="Reason - ", value=reason)    
        embed.set_footer(text=f"Banned By Mod/Owner - {ctx.message.author}", icon_url=ctx.author.avatar_url)
        await member.send(embed=embed)
        await logs.send(embed=embed)

    @commands.command(aliases=["purge"])
    @commands.has_role("Staff")
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(title="Message Purged", colour=discord.Color.from_rgb(255, 215, 0))

        embed.add_field(name="Ammount Of Message Purged - ", value=amount)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Mod(bot))
    print("\nMod.py Loaded\n")