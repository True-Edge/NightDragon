@bot.event
async def on_ready():
    print('----------\nLogged As [{0.user}]\nUser ID: [{0.user.id}]\n----------'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=3, name="[True Edge]"))
