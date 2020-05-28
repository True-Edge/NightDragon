@bot.command()
@commands.is_owner()
async def cprefix(ctx, prefix=None):
    if prefix == None:
        ctx.send("Prefix cannot be empty!")

    with open('System/Prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('System/Prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

    await ctx.send(f"Prefix Has Changed To {prefix}")