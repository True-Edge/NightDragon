@bot.event
async def on_guild_join(guild):
    with open('System/serverprefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'n$'

    with open('System/serverprefix.json', 'r') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('System/serverprefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('System/serverprefix.json', 'r') as f:
        json.dump(prefixes, f, indent=4)

@bot.commands()
async def chp(ctx, prefix):
    with open('System/serverprefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('System/serverprefix.json', 'r') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f"Prefix Changed To: {prefix}")