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
import sqlite3
from datetime import date
from os import system
pre = sqlite3.connect(database="System/Prefixes.db")
cre = pre.cursor()

def get_sprefix(bot, message):
    before_data = cre.execute("SELECT * FROM sprefix")
    data = before_data.fetchall()

    return data[0][1]

before_owner_id = cre.execute("SELECT * FROM pri")
owner_id = before_owner_id.fetchall()[0]
guild_id = 413632902480396298
load_dotenv()
token = os.getenv("TOKEN")

bot = commands.AutoShardedBot(command_prefix = get_sprefix, case_insensitive=True, status=discord.Status.idle, activity=discord.Activity(type=2, name="System Mainframe"))
bot.remove_command('help')

async def change_stat():
    await bot.wait_until_ready()
    while not bot.is_closed():
        for guild in bot.guilds:
            x = guild.member_count
            Status = ["getthisserverprefix","wollycraft.ml", f"Over {x} user"]
            for st in Status:
                await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=3, name=st))
                await asyncio.sleep(8)

@bot.event
async def on_ready():
    print(f'----------\nLogged As [{bot.user}]\nUser ID: [{bot.user.id}]\n----------')
    bot.loop.create_task(change_stat())

@bot.listen()
async def on_message(message):
    if message.content.startswith("getthisserverprefix"):
        channel = message.channel
        await channel.send(f"This server prefix is {await bot.get_prefix(message)}")

for command in os.listdir('commands'):
    if command.endswith('.py'):
        with open(f'commands/{command}') as rk:
            exec(rk.read())

bot.run(token)