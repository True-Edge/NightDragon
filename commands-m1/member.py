@bot.event
async def on_member_join(member: discord.Member):
        if str(member.guild.id) != "413632902480396298":
            pass                   
        else:
            r = get(member.guild.roles, name='[Not Verified]')
            await member.send("Welcome {member.mention}, Please Do {}verify To Start Verify!".format(member, pref))
            await member.add_roles(r)

