import discord
import json
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('System/serverprefix.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = 'n$'

        with open('System/serverprefix.json', 'r') as f:
            json.dump(prefixes, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('System/serverprefix.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('System/serverprefix.json', 'r') as f:
            json.dump(prefixes, f, indent=4)

    @commands.command()
    async def chp(self, ctx, prefix):
        with open('System/serverprefix.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('System/serverprefix.json', 'r') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f"Prefix Changed To: {prefix}")

def setup(bot):
    client.add_cog(Events(bot))


