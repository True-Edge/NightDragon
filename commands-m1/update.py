@bot.command()
async def update(self, ctx):
    if ctx.author.id in owner_id:
        embed = discord.Embed(title="Access Granted", description="Restarting Service ``TMUX``", color=discord.Color.from_rgb(255, 215, 0))
        await ctx.send(embed=embed)
        await asyncio.sleep(5)
        os.system("./stop.sh")
        sys.exit()
    else:
        embed = discord.Embed(title="Access Denied", description=f"{ctx.author} ID is not in database", color=discord.Color.from_rgb(255,215,0))
        await ctx.send(embed=embed)