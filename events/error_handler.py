import discord
from discord.ext import commands
embed = discord.Embed()
@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed.title = "Error"
        embed.description = f"Uh oh! Looks like the command you tried to execute was missing a argument. Please try again."
    elif isinstance(error, commands.CommandNotFound):
        embed.title = "Error"
        embed.description = "Uhhh, This is Awkward... Looks like i don't have that command programmed into my database..."
    elif isinstance(error, commands.MissingAnyRole):
        embed.title = "Error"
        embed.description = "You don't have the role to do that!"
    elif isinstance(error, commands.CommandError):
        embed.title = "Error"
        embed.description = "Looks like the command failed to execute. Please try again later."