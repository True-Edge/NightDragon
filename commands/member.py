@bot.event
async def on_guild_join(guild):
    with open('System/Prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'n$'

    with open('System/Prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

@bot.event
async def on_guild_remove(guild):
    with open('System/Prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop[str(guild.id)]

    with open('System/Prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)