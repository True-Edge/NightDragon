import discord
import json
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from dotenv import load_dotenv
from pathlib import Path
import youtube_dl

import asyncio
import datetime
import time
import sys

import os
import logging
import random
from os import system

pref = open("System/prefix.u.g", "r").read()
Status = [f"{pref} ./[True Edge]", "wollycraft.net"]
owner_id = 413632156061925380, 376102007779360769, 300126997718237195, 529290942306320384, 615942459943288843
guild_id = 413632902480396298
load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix = pref, case_insensitive=True, status=discord.Status.idle, activity=discord.Activity(type=2, name="System Mainframe"))
bot.remove_command('help')

async def change_stat():
    await bot.wait_until_ready()
    while not bot.is_closed():
        st = random.choice(Status)
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=3, name=st))
        await asyncio.sleep(10)
@bot.event
async def on_ready():
    print('----------\nLogged As [{0.user}]\nUser ID: [{0.user.id}]\n----------'.format(bot))

for cog in os.listdir('commands'):
    if cog.endswith(".py"):
        try:
            cog = f"commands.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as err:
            print("An Error Has Occured, Logs Has Been Generated")
            logging.basicConfig(filename="Logs/log.txt", filemode='w+', format='%(levelname)s > %(message)s')
            logging.error("An Error Occured.", exc_info=True)

for extra_command in os.listdir('commands-m1'):
    if extra_command.endswith('.py'):
            with open(f'commands-m1/{extra_command}') as rk:
                exec(rk.read())

bot.loop.create_task(change_stat())
bot.run(token)