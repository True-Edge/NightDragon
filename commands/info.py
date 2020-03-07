import discord
from discord.ext import commands

import os

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        urli = open('.\System\Invite-Link', 'r').read()

    @commands.command()
    async def info(ctx):
        await ctx.send("{urli}")

def setup(bot):
    bot.add_cog(Info(bot))
    print("\nInfo.py Loaded\n")