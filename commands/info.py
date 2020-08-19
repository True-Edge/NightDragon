@bot.command()
async def info(ctx):
    await ctx.message.delete()

    embed1 = discord.Embed(
        title='About Me',
        colour=discord.Color.from_rgb(215, 255, 0),
        description="Created At: 14th March 2019\n[Discord Server](discord.gg/GhPyRgx)\n[Invite Me!](https://discordapp.com/api/oauth2/authorize?client_id=648085129599647744&permissions=2147483127&scope=bot)")

    await ctx.send(embed=embed1)        
        