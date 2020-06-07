@bot.command(description="Reads ID db")
async def list_db(ctx):
    cru.execute("SELECT * FROM PRI")
    data = cru.fetchall()
    for list1 in data:
        await ctx.send(f"{list1}")

