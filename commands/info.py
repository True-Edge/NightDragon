@bot.command()
async def info(ctx):
    await ctx.message.delete()
    urli = open('System/Invite-Link', 'r').read()
    embed1 = discord.Embed(
        title='About Me',
        colour=discord.Color.from_rgb(215, 255, 0),
        description="Created At: 14th March 2019\n[Discord Server](https://discord.gg/tehurtf)\n[Invite Me!]({})".format(urli)
        )

    await ctx.send(embed=embed1)        
        