@bot.command(description="Changes Bot Prefix||<prefix>")
@commands.is_owner()
async def cprefix(ctx, prefix=None):
    await ctx.message.delete()
    member = discord.Member
    if prefix == None or prefix == member.mention:
        await ctx.send("Prefix cannot be empty or mentions!")
    else:
        try:
            message = discord.Message
            cre.execute("UPDATE sprefix SET prefix = $1 WHERE guildid = $2",(prefix, ctx.guild.id))
            pre.commit()
            await ctx.send(f"Changed Prefix To {prefix}")
        except:
            await ctx.send(f"Failed to change prefix to {prefix}")