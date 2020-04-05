import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(ctx):
        embed = discord.Embed(title="List Of Command", colour=discord.Color.from_rgb(255, 215, 0))

        embed.add_field(name="join", value="Join User's Voice Channel", inline=False)
        embed.add_field(name="leave", value="Clear Music Queues And Leave Voice Channel", inline=False)
        embed.add_field(name="volume <1-100>", value="Change Bot Music Volume", inline=False)
        embed.add_field(name="now", value="Shows Current Playing Song", inline=False)
        embed.add_field(name="pause", value="Pauses Current Playing Song", inline=False)
        embed.add_field(name="resume", value="Resume Paused Song", inline=False)
        embed.add_field(name="stop", value="Stop All Songs And Clear Queue")
        embed.add_field(name="skip", value="Skips Song If User Is Requester, If Not, Start Vote.", inline=False)
        embed.add_field(name="queue", value="Shows Queue", inline=False)
        embed.add_field(name="shuffle", value="Shuffles The Queue", inline=False)
        embed.add_field(name="remove <value>", value="Remove Song From Queue", inline=False)
        embed.add_field(name="loop", value="Loops Current Songs")
        embed.add_field(name="play <name/links>", value="Play Song, Will Add Next Requested Music To Queue", inline=False)
        embed.add_field(name="info", value="Shows Bot Info", inline=False)
        embed.add_field(name="ping", value="Returns Pong!", inline=False)
        embed.add_field(name="stat <mention member>", value="Shows A User Info")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))