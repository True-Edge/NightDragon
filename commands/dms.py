@bot.command()
@commands.has_role("Staff")
async def dm(ctx, member: discord.Member, *,reason="None"):
    await member.send(reason)
    await ctx.send("Message Sended")