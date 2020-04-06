import discord
from discord.ext import commands

pref = open("System/prefix.u.g", "r").read()

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, args=None):
        embed = discord.Embed(title="List Of Command", colour=discord.Color.from_rgb(255, 215, 0))
        
        if args == None:
            embed.add_field(name="Command", value=f"{pref}help command",)
            embed.add_field(name="Mods Command", value=f"{pref}help mod",)
            embed.add_field(name="Music Command", value=f"{pref}help music",)
            embed.set_footer(text=f"Requested By -> {ctx.author}", icon_url=ctx.author.avatar_url)

        if args == 'command':
            embed.add_field(name="info", value="Shows Bot Info", inline=False)
            embed.add_field(name="stat <mention member>", value="Shows A User Info", inline=False)
            embed.add_field(name="meme", value="Choose Random Meme From Reddit :)", inline=False)
            embed.set_footer(text=f"Requested By -> {ctx.author}", icon_url=ctx.author.avatar_url)
        
        if args == 'music':
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
            embed.set_footer(text=f"Requested By -> {ctx.author}", icon_url=ctx.author.avatar_url)

        if args == 'mod':
            embed.add_field(name="kick <member> <reason>", value="Kick A Member Out The Guild", inline=False)
            embed.add_field(name="ban <member> <reason>", value="Ban a member", inline=False)
            embed.add_field(name="clear/purge <amount>", value="Clear Messages With The Amount Provided", inline=False)
            embed.set_footer(text=f"Requested By -> {ctx.author}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))