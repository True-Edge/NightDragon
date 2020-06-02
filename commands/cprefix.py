@bot.command(description="Changes Bot Prefix||<prefix>")
@commands.is_owner()
async def cprefix(ctx, prefix=None):
    if prefix == None or discord.Member.mention:
        await ctx.send("Prefix cannot be empty or mentions!")
    else:
        try:
            with open('System/Prefixes.json', 'r') as f:
                prefixes = json.load(f)

            prefixes[str(ctx.guild.id)] = prefix

            with open('System/Prefixes.json', 'w') as f:
                json.dump(prefixes, f, indent = 4)

            await ctx.send(f"Prefix Has Changed To {prefix}")
        except:
            await ctx.send(f"Failed To Change Prefix To {prefix}")