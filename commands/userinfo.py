@bot.command()
async def stat(ctx, member: discord.Member):
    roles = [role for role in member.roles]
    x = member.joined_at.date()
    y = date.today()
    fvalue = y - x
    if fvalue.days < 7:
        fresult = "No"

    if fvalue.days >= 7:
        fresult = "Yes"

    embed = discord.Embed(title=f"{member.name} Info", colour=discord.Color.from_rgb(255, 215, 0))
    embed.add_field(name="Name - ", value=member, inline=True)
    embed.add_field(name="In Guild Name - ", value=member.nick, inline=True)
    embed.add_field(name="Joined At - ", value=member.joined_at.strftime("%d %b %Y"), inline=True)
    embed.add_field(name="Created At - ", value=member.created_at.strftime("%#d %b %Y"), inline=True)
    embed.add_field(name="Bot? - ", value=member.bot, inline=True)
    embed.add_field(name="Qualification For Mod", value=f"{fvalue.days} Days, {fresult}")
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested By -> {ctx.author.name}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)