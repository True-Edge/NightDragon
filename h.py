import hata
import os
import dotenv
from hata.ext.commands import setup_ext_commands
from hata import Client, start_clients
from hata import Embed
from hata import Color
from dotenv import load_dotenv
load_dotenv()
Token = os.environ.get("TOKEN")
Bot = Client(Token)
setup_ext_commands(Bot, 'n$')

owner_id = 413632156061925380
owner_id2 = 300126997718237195

@Bot.commands
async def update(client, message):
    if message.author.id != owner_id and message.author.id != owner_id2:
        embed1 = Embed(title="ID Not Match", description=f"```{message.author} ID Does Not Match With The System Provided ID!```", color=Color.from_rgb(255, 215, 0))
        await client.message_create(message.channel, embed1=embed1)
    else:
        embed = Embed(title="ID Matched", description="```Bot Updating....```", color=Color.from_rgb(255, 215, 0))
        await client.message_create(message.channel, embed=embed)
        os.system('./stop.sh')

start_clients()