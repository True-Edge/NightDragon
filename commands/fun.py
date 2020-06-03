@bot.command(description="Random command")
async def slap(ctx, member=bot.guilds):
    a = random.choice(member)
    await ctx.send(f"{ctx.author} Slapped {a}")