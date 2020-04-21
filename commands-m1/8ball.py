@bot.command()
async def question(ctx, args):
    A = (["Yes", "No", "I don't think so"])
    embed = discord.Embed(title="8 Ball Question", colour=discord.Color.from_rgb(215, 255, 0))
        embed.add_field(name="Question >", value=f"{args}")
        embed.add_field(name="Answer >", value=random.choice(A))
    await ctx.send(embed=embed)