import discord
from discord.ext import commands
from discord.utils import get

pref = open(".\system\prefix.u.g", "r").read()

class greetCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        r = get(member.guild.roles, name='[Not Verified]')
        await member.send("Welcome @{}, Please Do {}verify To Start Verify!".format(member, pref))
        await member.add_roles(r)
        
def setup(bot):
    bot.add_cog(greetCog(bot))