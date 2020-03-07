import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["h"])
    async def chelp(ctx):
        embed = discord.Embed(
            title = "Commands",
            color = discord.Colour.blue()
        )

        embed.set_footer("Created By DMNight6")
        embed.add_field(name='ping', value='Find Bot Latency', inline=False)
        embed.add_field(name='play', value='/play <url>', inline=False)
        embed.add_field(name='join', value='Join [Message Author] Voice C.', inline=False)
        embed.add_field(name='leave', value='Leaves Voice C.', inline=False)
        embed.add_field(name='pause', value='Pauses Current Song', inline=False)
        embed.add_field(name='stop', value='Stop Current Song', inline=False)
        embed.add_field(name='resume', value='Resume paused Song', inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
    print("\n\nHelp.py Has Loaded\n")