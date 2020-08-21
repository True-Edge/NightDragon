@bot.listen()
async def on_guild_join(guild):
    cre.execute("INSERT INTO sprefix (guildid) VALUES (?)",(guild.id))
    pre.commit()

@bot.listen()
async def on_guild_remove(guild):
    message = discord.Message
    before_prec = cre.execute("SELECT * FROM sprefix")
    after_prec = before_prec.fetchall()
    cre.execute("DELETE FROM sprefix WHERE guildid = $1 AND prefix = $2",(guild.id, await bot.get_prefix(message)))
    pre.commit()