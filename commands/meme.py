import discord
import praw
from discord.ext import commands

reddit = praw.Reddit(client_id="dppEVP0A5XgxfQ", client_secret="VvzhNIrQkJGtQdrduzK87X76ZYs", user_agent="u/dmnight6 :)")

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(colour=discord.Color.from_rgb(255, 215, 0))
        embed.set_image(url=submission.url)
        embed.set_footer(text=f"Requested By -> {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Meme(bot))