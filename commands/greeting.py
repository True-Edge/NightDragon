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

    @commands.command()
    async def pingr(self, ctx):
        user = ctx.message.author
        r2 = get(user.guild.roles, name="[PING]")
        if get(user.roles, name='[PING]'):
            await user.send("You Already Have The Ping Role!")
        else:
            await user.add_roles(r2)
            await user.send(':white_check_mark: You Have Assigned With The "{}" Role!'.format(r2))
        


def setup(bot):
    bot.add_cog(greetCog(bot))