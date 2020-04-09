import discord
from discord.ext import commands

import os
import asyncio
import sys
owner_id = 413632156061925380
owner_id2 = 300126997718237195
pref = open("System/prefix.u.g", "r").read()
bot = commands.Bot(command_prefix = pref, case_insensitive=True)

class ModuleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def update(self, ctx):
        if ctx.message.author.id != owner_id or ctx.message.author.id != owner_id2:
            await ctx.send("You Have No Permission To Do This")
        else:
            try:
                os.system("./stop.sh")
                sys.exit()
            except:
                pass
         
def setup(bot):
    bot.add_cog(ModuleCog(bot))