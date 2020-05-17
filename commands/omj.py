@bot.event
async def on_member_join(member):
    if member.guild.id == guild_id:
        embed = discord.Embed(title=f"Welcome! {member}", description=f"Welcome To **{member.guild}**! <@{member.id}>", color=discord.Color.from_rgb(255, 215, 0))
        await member.send(embed=embed)