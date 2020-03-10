import discord
from discord.ext import commands
from discord.utils import get

import asyncio
import datetime
import sys

import os
import logging

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
        except Exception as err:
            print(f"{cog} Can't Load")
            raise err

bot.run(token)