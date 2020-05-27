@bot.command()
async def cprefix(ctx, prefix):
    if prefix == None:
        ctx.send("Prefix cannot be empty!")

    with open('System/Prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('System/Prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)