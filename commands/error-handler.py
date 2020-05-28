@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="Unknown Command!", description=f"Invalid command provided",color=discord.Color.from_rgb(255, 215, 0))
    embed.set_footer(text=f"Attempted By -> {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)