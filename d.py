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
import random
from os import system

import hata
import os
import dotenv
from hata.ext.commands import setup_ext_commands
from hata import Client, start_clients
from hata import Embed
from hata import Color

pref = open("System/prefix.u.g", "r").read()
owner_id = "413632156061925380"
guild_id = "413632902480396298"
load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix = pref, case_insensitive=True, status=discord.Status.idle, activity=discord.Game(name="Loading..."))
client = commands.Bot(command_prefix = pref, case_insensitive=True)
bot.remove_command('help')
client.remove_command('help')

Token = os.environ.get("TOKEN")
Bot = Client(Token)
setup_ext_commands(Bot, 'n$')

owner_id1 = 413632156061925380
owner_id2 = 300126997718237195
owner_id3 = 376102007779360769

@Bot.commands
async def update(client, message):
    if message.author.id != owner_id1 and message.author.id != owner_id2 and message.author.id != owner_id3:
        embed = Embed(title="ID Not Match", description=f"```Your ID Does Not Match With Author ID!```", color=Color.from_rgb(255, 215, 0))
        await client.message_create(message.channel, embed=embed)
    else:
        embed = Embed(title="ID Matched", description="```Bot Updating....```", color=Color.from_rgb(255, 215, 0))
        await client.message_create(message.channel, embed=embed)
        os.system('./stop.sh')
        
@Bot.events
async def ready(client):
    print(f"{client:f} Is Ready!")

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
        with open(f'commands-m1/{cogm2}') as rk:
            exec(rk.read())

start_clients()            
bot.run(token)