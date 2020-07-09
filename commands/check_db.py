@bot.command(description="Reads ID db")
async def list_db(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="DB List")
    cre.execute("SELECT * FROM pri")
    data = cre.fetchall()
    for list1 in data:
        embed.add_field(name="ID", value=list1)
        
    await ctx.send(embed=embed)