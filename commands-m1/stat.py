zz@bot.event
async def on_ready():
    print('----------\nLogged As [{0.user}]\nUser ID: [{0.user.id}]\n----------'.format(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="{} ./[True Edge]").format(pref))
