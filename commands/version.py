@bot.command()
async def version(ctx):
    embed = discord.Embed(title="Bot Addition Info", color=discord.Color.from_rgb(255, 215, 0))
    embed.add_field(name="Version", value="1.4")
    embed.add_field(name="Release Version", value="[Stable]")
    await ctx.send(embed=embed)