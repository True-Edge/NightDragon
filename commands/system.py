import discord
from discord.ext import commands

import os
owner_id = "413632156061925380"
pref = open(".\system\prefix.u.g", "r").read()
bot = commands.Bot(command_prefix = pref, case_insensitive=True)

class ModuleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def reboot(self, ctx):
        if str(ctx.message.author.id) != owner_id:
            await ctx.send("You Have No Permission To Do This")
        else:
            try:
                await bot.close()
            except:
                pass
            finally:
                os.system("py bot.py")
    
    @commands.command(hidden=True)
    async def shutdown(self, ctx):
        if str(ctx.message.author.id) != owner_id:
            await ctx.send("Begone Mortals, You Are Not Allowed To Use This Command.")
        else:
            try:
                await bot.close()
            except:
                pass
            
def setup(bot):
    bot.add_cog(ModuleCog(bot))