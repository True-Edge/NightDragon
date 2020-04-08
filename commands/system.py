import discord
from discord.ext import commands

import os
import asyncio
import sys
owner_id = "413632156061925380"
pref = open("System/prefix.u.g", "r").read()
bot = commands.Bot(command_prefix = pref, case_insensitive=True)

class ModuleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def update(self, ctx):
        if str(ctx.message.author.id) != owner_id:
            await ctx.send("You Have No Permission To Do This")
        else:
            try:
                os.system("./stop.sh")
                sys.exit()
            except:
                pass
         
def setup(bot):
    bot.add_cog(ModuleCog(bot))