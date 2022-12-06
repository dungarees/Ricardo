import discord
from discord.ext import commands
from colorama import Fore, init


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.LIGHTGREEN_EX}   [+]   Ping command is ready')  
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
        
        
async def setup(bot):
    await bot.add_cog(ping(bot))
        
    