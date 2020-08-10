@bot.command(description="Fetch System Resources")
async def system_resource(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="System Resources", color=discord.Color.from_rgb(255, 215, 0))
    embed.add_field(name="OS", value=sys.platform)
    embed.add_field(name="CPU Usage", value=f"{psutil.cpu_percent(interval=None)}%")
    embed.add_field(name="RAM Usage", value=f"{psutil.virtual_memory().percent}%")
    embed.set_footer(text=f"System Info Requested By: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)