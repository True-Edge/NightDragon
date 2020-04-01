import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from dotenv import load_dotenv
from pathlib import Path
import youtube_dl

import asyncio
import datetime
import sys

import os
import logging
from os import system

pref = open("System/prefix.u.g", "r").read()
owner_id = "413632156061925380"
guild_id = "413632902480396298"
bot = commands.Bot(command_prefix = pref, case_insensitive=True, status=discord.Status.idle, activity=discord.Game(name="Loading..."))
load_dotenv()
token = os.getenv("TOKEN")

for cog in os.listdir('commands'):
    if cog.endswith(".py"):
        try:
            cog = f"commands.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as err:
            print("An Error Has Occured, Logs Has Been Generated")
            logging.basicConfig(filename="Logs/log.txt", filemode='w+', format='%(levelname)s > %(message)s')
            logging.error("An Error Occured.", exc_info=True)

for cogm2 in os.listdir('commands-m1'):
    if cogm2.endswith('.py'):
        try:
            with open(f'commands-m1/{cogm2}') as rk:
                exec(rk.read())
        except Exception as err2:
            logging.basicConfig(filename="Logs/log-m2.txt", filemode='w+', format='%(levelname)s > %(message)s')
            logging.error("An Error Occured", exc_info=True)

bot.run(token)