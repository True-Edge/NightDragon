@bot.command()
async def stat(ctx, member: discord.Member):
    embed = discord.Embed(title=f"{member} Info", colour=discord.Color.from_rgb(255, 215, 0))

    embed.add_field(name=f"Name - {member}")
    embed.add_field(name=f"In Guild Name - {member.name}")
    embed.add_field(name="Joined At - ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%N -> %p UTC"))
    embed.add_field(name="Created At - ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%N -> %p UTC"))
    embed.add_field(name="Bot?", value=member.bot)
    embed.set_thumbnail(member.avatar_url)
    embed.set_footer(text=f"Requested By > {ctx.author.name}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)