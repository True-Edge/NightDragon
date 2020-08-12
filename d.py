import discord, praw, lavalink, re
import os, sys, sqlite3, json, psutil
import time, datetime
import math, random, asyncio, itertools, functools

from discord.ext import commands
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

bot = commands.Bot(command_prefix = get_sprefix, case_insensitive=True, status=discord.Status.idle, activity=discord.Activity(type=2, name="System Mainframe"))
bot.remove_command('help')

async def change_stat():
    Status = ["serverprefix", "System Resources."]
    await bot.wait_until_ready()
    while not bot.is_closed():
        for st in Status:
            await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=3, name=st))
            await asyncio.sleep(8)

@bot.listen()
async def on_ready():
    print(f'----------\nLogged As [{bot.user}]\nUser ID: [{bot.user.id}]\n----------')
    for command in os.listdir('commands'):
        if command.endswith('.py'):
            with open(f'commands/{command}') as rk:
                exec(rk.read())
    for events in os.listdir('events'):
        if events.endswith('.py'):
            with open(f"events/{events}") as rk1:
                exec(rk1.read())
    bot.loop.create_task(change_stat())

bot.run(token)