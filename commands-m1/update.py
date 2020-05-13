@bot.command()
async def update(ctx):
    if ctx.author.id in owner_id:
        embed = discord.Embed(title="Access Granted", description="```Updating```", color=discord.Color.from_rgb(255, 215, 0))
        await ctx.send(embed=embed)
        os.system("stop.sh")
    else:
        embed = discord.Embed(title="Access Denied", description=f"{ctx.author} ID is not in database", color=discord.Color.from_rgb(255,215,0))
        await ctx.send(embed=embed)