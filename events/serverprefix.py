@bot.listen()
async def on_message(message):
    if message.content.startswith("serverprefix"):
        channel = message.channel
        await channel.send(f"This server prefix is {await bot.get_prefix(message)}")