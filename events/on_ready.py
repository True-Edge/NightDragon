async def change_stat():
    Status = ["serverprefix", "System Resources."]
    await bot.wait_until_ready()
    while not bot.is_closed():
        for st in Status:
            await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=3, name=st))
            await asyncio.sleep(8)

@bot.listen()
async def on_ready():
    print(f'----------\nLogged As [{bot.user}]\nUser ID: [{bot.user.id}]\n----------')
    bot.loop.create_task(change_stat())
    bot.load_extension("Music.music")