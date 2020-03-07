import discord
from discord.ext import commands
from discord.utils import get

import asyncio
import datetime
import sys

import os

pref = open(".\system\prefix.u.g", "r").read()
owner_id = "413632156061925380"
bot = commands.Bot(command_prefix = pref, case_insensitive=True)
token = open(".\system\Token.u.g", 'r').read()

@bot.event
async def on_ready():
    print('----------\nLogged As [{0.user}]\nUser ID: [{0.user.id}]\n----------'.format(bot))
    return await bot.change_presence(activity=discord.Activity(type=1, name="[True Edge]", url="https://twitch.tv/dmnight6"))

for cog in os.listdir('.\\commands'):
    if cog.endswith(".py"):
        try:
            cog = f"commands.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} Can't Load")
            raise e

@bot.command(hidden="true", aliases=["r"])
async def mreload(ctx):
    if str(ctx.message.author.id) == owner_id:
        await bot.unload_extension(cog)
        await bot.load_extension(cog)
    else:
        await ctx.send(":negative_squared_cross_mark: You Have No Permission To Do This!")
        await ctx.send(ctx.message.author.id)
        await ctx.send(owner_id)
        


bot.run(token)
