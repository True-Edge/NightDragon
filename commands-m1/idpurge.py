@client.command(aliases=["clearid"])
async def purgeid(ctx, amount: int):
    if ctx.message.author.id == owner_id:
        await ctx.channel.purge(limit=amount + 1)
    else:
        await ctx.send("This is a command for @DMNight6.")