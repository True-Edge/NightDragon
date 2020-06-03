@bot.command()
async def slap(ctx, member=discord.Member):
    a = random.choice(member)
    await ctx.send(f"{ctx.author} Slapped {a}")