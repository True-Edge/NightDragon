import discord
from discord.ext import commands

import os
import sys
import asyncio

owner_id = 413632156061925380
owner_id2 = 300126997718237195
pref = open("System/prefix.u.g", "r").read()
bot = commands.Bot(command_prefix = pref, case_insensitive=True)

class ModuleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def update(self, ctx):
        if ctx.author.id != owner_id and ctx.author.id != owner_id2:
            await ctx.send("You Have No Permission To Do This")
        else:
            try:
                sys.exit()
                os.system("./stop.sh")
            except:
                pass
         
def setup(bot):
    bot.add_cog(ModuleCog(bot))