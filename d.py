import discord, praw, lavalink, re
import os, sys, sqlite3, json, psutil
import time, datetime
import math, random, asyncio, itertools, functools

from discord.ext import commands, menus
from discord.utils import get
from discord import FFmpegPCMAudio, utils
from async_timeout import timeout
from pathlib import Path
from datetime import date
from os import system
from sys import platform
from dotenv import load_dotenv

load_dotenv()

pre = sqlite3.connect(database="System/Prefixes.db")
cre = pre.cursor()

before_owner_id = cre.execute("SELECT * FROM pri")
owner_id = before_owner_id.fetchall()[0]

token = os.environ.get("TOKEN")
guild_id = 413632902480396298

def get_sprefix(bot, message):
    before_data = cre.execute("SELECT * FROM sprefix")
    data = before_data.fetchall()
    return data[0][1]

bot = commands.AutoShardedBot(command_prefix = get_sprefix, case_insensitive=True, status=discord.Status.idle, activity=discord.Activity(type=2, name="System Mainframe"))
bot.remove_command('help')

for events in os.listdir('events'):
    if events.endswith('.py'):
        with open(f"events/{events}") as rk1:
            exec(rk1.read())

bot.run(token)