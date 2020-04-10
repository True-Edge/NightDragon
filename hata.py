import hata
import dotenv
import os
from hata import Client, start_clients
from hata.ext.commands import setup_ext_commands
from hata.ext.commands import checks
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("TOKEN")
pref = open("System/prefix.u.g", 'r').read()
bot = Client(token)

setup_ext_commands(bot, pref)

@bot.commands(checks=[checks.owner_only()])
async def update(message):
    await client.message_create("Updating....")
    os.system("./stop.sh")

start_clients()
