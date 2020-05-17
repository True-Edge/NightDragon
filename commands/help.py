@bot.command()
async def help(ctx, args=None):
    user = ctx.author
    embed = discord.Embed(title="List Of Command", colour=discord.Color.from_rgb(255, 215, 0))
        
    if args == None:
        embed.add_field(name="Command", value=f"{pref}help command",)
        embed.add_field(name="Mods Command", value=f"{pref}help mod",)
        embed.add_field(name="Music Command", value=f"{pref}help music",)
        embed.set_footer(text=f"Requested By -> {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    if args == 'command':
        embed1 = discord.Embed(title="Command", color=discord.Color.from_rgb(255,215,0))
        embed1.add_field(name="info", value="Shows Bot Info", inline=False)
        embed1.add_field(name="stat <mention member>", value="Shows A User Info", inline=False)
        embed1.add_field(name="meme", value="Choose Random Meme From Reddit :)", inline=False)
        embed1.set_footer(text=f"Requested By -> {ctx.author}", icon_url=ctx.author.avatar_url)
        await user.send(embed=embed1)
        await ctx.send(" :inbox_tray: | Please Check Your DM :) ")

    if args == 'music':
        embed2 = discord.Embed(title="Music Command", color=discord.Color.from_rgb(255,215,0))
        embed2.add_field(name="join", value="Join User's Voice Channel", inline=False)
        embed2.add_field(name="leave", value="Clear Music Queues And Leave Voice Channel", inline=False)
        embed2.add_field(name="volume <1-100>", value="Change Bot Music Volume", inline=False)
        embed2.add_field(name="now", value="Shows Current Playing Song", inline=False)
        embed2.add_field(name="pause", value="Pauses Current Playing Song", inline=False)
        embed2.add_field(name="resume", value="Resume Paused Song", inline=False)
        embed2.add_field(name="stop", value="Stop All Songs And Clear Queue")
        embed2.add_field(name="skip", value="Skips Song If User Is Requester, If Not, Start Vote.", inline=False)
        embed2.add_field(name="queue", value="Shows Queue", inline=False)
        embed2.add_field(name="shuffle", value="Shuffles The Queue", inline=False)
        embed2.add_field(name="remove <value>", value="Remove Song From Queue", inline=False)
        embed2.add_field(name="loop", value="Loops Current Songs")
        embed2.add_field(name="play <name/links>", value="Play Song, Will Add Next Requested Music To Queue", inline=False)
        embed2.set_footer(text=f"Requested By -> {ctx.author}", icon_url=ctx.author.avatar_url)
        await user.send(embed=embed2)
        await ctx.send(" :inbox_tray: | Please Check Your DM :) ")

    if args == 'mod':
        r - get(ctx.guild.roles, "Staff")
        if user != r:
            await ctx.send("You have no permission to do this")
        else:
            embed3 = discord.Embed(title="Mod Command", color=discord.Color.from_rgb(255,215,0))
            embed3.add_field(name="kick <member> <reason>", value="Kick A Member Out The Guild", inline=False)
            embed3.add_field(name="ban <member> <reason>", value="Ban a member", inline=False)
            embed3.add_field(name="clear/purge <amount>", value="Clear Messages With The Amount Provided", inline=False)
            embed3.set_footer(text=f"Requested By -> {ctx.author}", icon_url=ctx.author.avatar_url)
            await user.send(embed3=embed3)
            await ctx.send(" :inbox_tray: | Please Check Your DM :) ") 