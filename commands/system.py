import discord
from discord.ext import commands

import os
import asyncio
import sys
owner_id = "413632156061925380"
def serverprefix(bot, message):
    with open('System/serverprefix.json', 'r') as f:
        prefixes = json.load(f)
    
    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = serverprefix, case_insensitive=True)

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