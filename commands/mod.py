@bot.command(description="Kick member out from the guild||<member> <reason>")
@commands.has_role("Staff")
async def kick(ctx, member: discord.Member, *, reason="None"):
    await member.kick(reason=reason)
    logs = get(ctx.guild.channels, name="logs")
    embed = discord.Embed(title="Member Kicked", colour=discord.Color.from_rgb(255, 215, 0))
        
    embed.add_field(name=f"{member} Was Kicked By -", value=ctx.author.mention)
    embed.add_field(name="Reason - ", value=reason)
    embed.set_footer(text=f"Kicked By Mod/Owner - {ctx.message.author}", icon_url=ctx.author.avatar_url)
    await member.send(embed=embed)
    await logs.send(embed=embed)

@bot.command(description="Bans member from the guild||<member> <reason>")
@commands.has_role("Staff")
async def ban(ctx, member: discord.Member, *, reason="None"):
    await member.ban(reason=reason)
    logs = get(ctx.guild.channels, name="logs")
    embed = discord.Embed(title="Member Banned", colour=discord.Color.from_rgb(255, 215, 0))

    embed.add_field(name=f"{member} Was Banned By - ", value=ctx.author.mention)
    embed.add_field(name="Reason - ", value=reason)    
    embed.set_footer(text=f"Banned By Mod/Owner - {ctx.message.author}", icon_url=ctx.author.avatar_url)
    await member.send(embed=embed)
    await logs.send(embed=embed)

@bot.command(aliases=["purge"], description="Clears number of message||<amount>")
@commands.has_role("Staff")
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    embed = discord.Embed(title="Message Purged", colour=discord.Color.from_rgb(255, 215, 0))

    embed.add_field(name="Amount Of Message Purged - ", value=amount)
    await ctx.send(embed=embed)