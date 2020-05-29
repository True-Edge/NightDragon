@bot.command(description="(Same function as clear but with specific ids)", aliases=["clearid"])
async def purgeid(ctx, amount: int):
    if ctx.message.author.id in owner_id:
        await ctx.channel.purge(limit=amount + 1)
    else:
        await ctx.send(f"You have no access")