@bot.command()
async def question(ctx, args):
    await ctx.send(random.choice(["Yes", "No", "I Don't think so"]))