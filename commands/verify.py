import discord, random, string
from discord.ext import commands
from discord.utils import get

randkey=""

class VerifyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verify(self, ctx):
        await ctx.send("To Verify, a code will be sent to you.\nOnce U Receive The Code, do 'n/verifykey <code>.'")
        user = ctx.message.author            
        logs = get(ctx.guild.channels, name='logs')
        await logs.send("'{}' Is Verifying.".format(user))
        if get(user.roles, name='[Verified]'):
            await ctx.send("'{}', You already have the role!".format(user))
            await logs.send("'{}' Attempted To Verify, User Failed To Verify As User Has The Role Already.")
        else:
            global randkey
            randkey = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            await ctx.author.send(randkey)

    @commands.command()
    async def verifykey(self, ctx, *, userkey):
        user = ctx.message.author
        logs = get(ctx.guild.channels, name='logs')
        r = get(ctx.guild.roles, name='[Verified]')
        global randkey
        if userkey == randkey:
            randkey=''
            await ctx.channels.purge(limit=1)
            await user.add_roles(r)
            await logs.send("'{}' Has Completed Verify".format(user))
            await user.send(":white_check_mark: You Have Successfully Verified!")
        else:
            await ctx.send("Wrong Code Entered, Please Try Again.")
    
            
def setup(bot):
    bot.add_cog(VerifyCog(bot))