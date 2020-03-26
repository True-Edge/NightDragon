import discord
from discord.ext import commands

import os

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        urli = open('System/Invite-Link', 'r').read()
        embed1 = discord.Embed(
            title='About Me',
            colour=discord.Color.from_rgb(215, 255, 0),
            description="Created At: 14th March 2019\n[Discord Server](https://discord.gg/tehurtf)\n[Invite Me!]({})".format(urli)
        )

        await ctx.send(embed=embed1)        
        
        

def setup(bot):
    bot.add_cog(Info(bot))
    print("\nInfo.py Loaded\n")