import discord
from discord.ext import commands

class ModuleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(allises="r",hidden="true")
    @commands.is_owner()
    async def sysload(self, *, module : str):
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            print("Falied To Reload!")
            raise e
        else:
            print("Reload Completed!")

def setup(bot):
    bot.add_cog(ModuleCog(bot))