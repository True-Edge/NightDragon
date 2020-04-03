@bot.command()
async def ui(ctx, member: discord.Menber):

    roles = [role for role in member.roles]

    embed = discord.Embed(title="{} Info", colour=discord.Color.from_rgb(255, 215,0))


    embed.set_footer(text=f"Requested By: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)

    embed.add_field(name=f"Name - {member}")
    embed.add_field(name=f"Guild Name - {member.display_name}")

    embed.add_field(name=f"Created At", value=member.created_at.strftime("%a, %m %b %d %y, %I:%M %p UTC"))
    embed.add_field(name=f"Joined At", value=member.joined_at.strftime("%a, %m %b %d %y, %I:%M %p UTC"))

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)
