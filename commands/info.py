import discord
from discord.ext import commands

import os

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        urli = open('.\System\Invite-Link', 'r').read()
        await ctx.send("{}".format(urli))

def setup(bot):
    bot.add_cog(Info(bot))
    print("\nInfo.py Loaded\n")