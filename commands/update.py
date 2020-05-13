import discord
from discord.ext import commands

import os
import sys
owner_id = 413632156061925380, 376102007779360769, 300126997718237195, 529290942306320384, 615942459943288843
class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def update(ctx):
        if ctx.author.id in owner_id:
            embed = discord.Embed(title="Access Granted", description="```Updating```", color=discord.Color.from_rgb(255, 215, 0))
            await ctx.send(embed=embed)
            os.system("./stop.sh")
        else:
            embed = discord.Embed(title="Access Denied", description=f"{ctx.author} ID is not in database", color=discord.Color.from_rgb(255,215,0))
            await ctx.send(embed=embed)