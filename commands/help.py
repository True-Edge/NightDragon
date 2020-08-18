@bot.command()
async def help(ctx, *, arguments=None):
    await ctx.message.delete()
    embed = discord.Embed()
    embed.description = "A list of command can be found in [here](https://codeberg.org/DMNight6/NightDragon/wiki/Bot-Commands)"
    await ctx.send(embed=embed)