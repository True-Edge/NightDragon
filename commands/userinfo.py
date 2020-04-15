import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stat(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]
        embed = discord.Embed(title=f"{member.name} Info", colour=discord.Color.from_rgb(255, 215, 0))

        embed.add_field(name="Name - ", value=member, inline=True)
        embed.add_field(name="In Guild Name - ", value=member.nick, inline=True)
        embed.add_field(name="Joined At - ", value=member.joined_at.strftime("%d %b %Y"), inline=True)
        embed.add_field(name="Created At - ", value=member.created_at.strftime("%#d %b %Y"), inline=True)
        embed.add_field(name="Bot? - ", value=member.bot, inline=True)
        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested By -> {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(UserInfo(bot))