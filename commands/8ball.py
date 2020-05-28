@bot.command(descripton="Ask a question||<question>")
async def question(ctx, *, args):
    A = (["Yes", "No", "I don't think so"])
    embed = discord.Embed(title="8 Ball Question", colour=discord.Color.from_rgb(255, 215, 0))
    embed.add_field(name="Question >", value=f"{args}", inline=False)
    embed.add_field(name="Answer >", value=random.choice(A), inline=False)
    embed.set_footer(text=f"Requested By > {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)