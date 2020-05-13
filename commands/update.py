import discord
from discord.ext import commands

import asyncio
import os
import sys
pref = open("System/prefix.u.g", "r").read()
bot = commands.Bot(command_prefix = pref, case_insensitive=True, status=discord.Status.idle, activity=discord.Game(name="Loading..."))
owner_id = 413632156061925380, 376102007779360769, 300126997718237195, 529290942306320384, 615942459943288843
class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def update(self, ctx):
        if ctx.author.id in owner_id:
            embed = discord.Embed(title="Access Granted", description="```Updating```", color=discord.Color.from_rgb(255, 215, 0))
            await ctx.send(embed=embed)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="Restarting System")
            await asyncio.sleep(10)
            os.system("./stop.sh")
            sys.exit()
        else:
            embed = discord.Embed(title="Access Denied", description=f"{ctx.author} ID is not in database", color=discord.Color.from_rgb(255,215,0))
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Update(bot))