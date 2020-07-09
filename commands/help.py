@bot.command()
async def help(ctx, *, arguments=None):
    await ctx.message.delete()
    if not arguments:
        cmds = {}
        with open('cmds/dcmds.json', 'w') as f:
            for command in bot.commands:
                desc = command.description.split('||')
                if command.name != 'help':
                    cmds[command.name] = {"desc": desc[0], 'syntax': desc[-1], 'required_roles': [], 'required_perms': []}
            json.dump(cmds, f)
            f.close()

        cmd_list = []
        for y in os.listdir('./cmds/'):
            with open('./cmds/'+y, 'r') as f:
                x = json.load(f)
            for i in x:
                if i.lower() != 'help':
                    cmd_list.append(i)
        p = commands.Paginator(prefix='```fix')
        for i in cmd_list:
            p.add_line(f'>> {i}')
        for page in p.pages:
            embed = discord.Embed(title='List of commands', color=discord.Color.from_rgb(255, 215, 0),
                            description=page)
            embed.set_footer(text=f'Requested by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)