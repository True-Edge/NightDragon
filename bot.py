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
import sys

import os
import logging
from os import system


pref = open("System/prefix.u.g", "r").read()
owner_id = "413632156061925380"
guild_id = "413632902480396298"
load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix = pref, case_insensitive=True, status=discord.Status.idle, activity=discord.Game(name="Loading..."))
client = commands.Bot(command_prefix = pref, case_insensitive=True, status=discord.Status.idle, activity=discord.Game(name="Loading..."))
bot.remove_command('help')

for clientloader in os.listdir('Loader'):
    if clientloader.endswith('.py'):
        with open(f'Loader/{clientloader}') as rkm2:
            exec(rkm2.read())
    
bot.run(token)