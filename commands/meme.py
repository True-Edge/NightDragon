reddit = praw.Reddit(client_id="dppEVP0A5XgxfQ", client_secret="VvzhNIrQkJGtQdrduzK87X76ZYs", user_agent="u/dmnight6 :)")

@bot.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 20)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    embed = discord.Embed(colour=discord.Color.from_rgb(255, 215, 0))
    embed.set_image(url=submission.url)
    embed.set_footer(text=f"Requested By -> {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)