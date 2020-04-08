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


def serverprefix(bot, message):
    with open('System/serverprefix.json', 'r') as f:
        prefixes = json.load(f)
    
    return prefixes[str(message.guild.id)]
    
pref = open("System/prefix.u.g", "r").read()
owner_id = "413632156061925380"
guild_id = "413632902480396298"
bot = commands.Bot(command_prefix = serverprefix, case_insensitive=True, status=discord.Status.idle, activity=discord.Game(name="Loading..."))
client = commands.Bot(command_prefix = serverprefix, case_insensitive=True, status=discord.Status.idle, activity=discord.Game(name="Loading..."))
load_dotenv()
token = os.getenv("TOKEN")

bot.remove_command('help')

for cog in os.listdir('commands-b'):
    if cog.endswith(".py"):
        try:
            cog = f"commands.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as err:
            print("An Error Has Occured, Logs Has Been Generated")
            logging.basicConfig(filename="Logs/log.txt", filemode='w+', format='%(levelname)s > %(message)s')
            logging.error("An Error Occured.", exc_info=True)

for cogm2 in os.listdir('commands-m1-b'):
    if cogm2.endswith('.py'):
        try:
            with open(f'commands-m1/{cogm2}') as rk:
                exec(rk.read())
        except Exception as err2:
            print("Error Occured, Log generated")
            logging.basicConfig(filename="Logs/log-m2.txt", filemode='w+', format='%(levelname)s > %(message)s')
            logging.error("An Error Occured", exc_info=True)

for cog01 in os.listdir('commands-c'):
    if cog01.endswith(".py"):
        try:
            cog01 = f"commands.{cog01.replace('.py', '')}"
            client.load_extension(cog01)
        except Exception as err:
            print("An Error Has Occured, Logs Has Been Generated")
            logging.basicConfig(filename="Logs/log.txt", filemode='w+', format='%(levelname)s > %(message)s')
            logging.error("An Error Occured.", exc_info=True)

for cog02 in os.listdir('commands-m1-c'):
    if cog02.endswith('.py'):
        try:
            with open(f'commands-m1/{cog02}') as rc:
                exec(rc.read())
        except Exception as err2:
            print("Error Occured, Log generated")
            logging.basicConfig(filename="Logs/log-m2.txt", filemode='w+', format='%(levelname)s > %(message)s')
            logging.error("An Error Occured", exc_info=True)

bot.run(token)