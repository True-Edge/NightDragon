import discord
import json
from discord.ext import commands,tasks
from discord.utils import get
from discord import FFmpegPCMAudio
from dotenv import load_dotenv
from pathlib import Path
import math
import random
import asyncio
import datetime
import time
import sys
import praw
import os
import datetime
from datetime import date
from os import system

def get_sprefix(bot, message):
    with open("System/Prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

owner_id = 413632156061925380, 376102007779360769, 300126997718237195, 529290942306320384, 615942459943288843
guild_id = 413632902480396298
load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix = get_sprefix, case_insensitive=True, status=discord.Status.idle, activity=discord.Activity(type=2, name="System Mainframe"))
bot.remove_command('help')

def sprefix():
    with open("System/Prefixes.json", "r") as f:
        pref = json.load(f)

    pref[str(message.guild.id)]

async def change_stat():
    await bot.wait_until_ready()
    while not bot.is_closed():
        for guild in bot.guilds:
            x = guild.member_count
            Status = ["wollycraft.ml", f"Over {x} user"]
            for st in Status:
                await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=3, name=st))
                await asyncio.sleep(8)

@bot.event
async def on_ready():
    print(f'----------\nLogged As [{bot.user}]\nUser ID: [{bot.user.id}]\n----------')
    bot.loop.create_task(change_stat())

for command in os.listdir('commands'):
    if command.endswith('.py'):
        with open(f'commands/{command}') as rk:
            exec(rk.read())

bot.run(token)