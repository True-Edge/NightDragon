import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stat(self, ctx, member: discord.Member):
        embed = discord.Embed(title=f"{member} Info", colour=discord.Color.from_rgb(255, 215, 0))

        embed.add_field(name="Name - ", value=member)
        embed.add_field(name="In Guild Name - ", value=member.name)
        embed.add_field(name="Joined At - ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%N -> %p UTC"))
        embed.add_field(name="Created At - ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%N -> %p UTC"))
        embed.add_field(name="Bot?", value=member.bot)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested By > {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)