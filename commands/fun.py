@bot.command(description="Random command")
async def slap(ctx, member=ctx.guild.member):
    a = random.choice(member)
    await ctx.send(f"{ctx.author} Slapped {a}")