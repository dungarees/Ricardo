import discord
import os, sys
from discord.ext import commands
from colorama import Fore, init

OWNER_ID = os.getenv("OWNER_ID")



class restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def restart_bot(): 
        os.execv(sys.executable, ['python'] + sys.argv)
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.LIGHTGREEN_EX}   [+]   Restart command is ready')  
        
    @commands.command()
    async def restart(self, ctx):
        if ctx.author.id == OWNER_ID:
            await ctx.send("Restarting bot...")
            restart.restart_bot()
        else:
            await ctx.send("You do not have permission to use this command.")
        
        
async def setup(bot):
    await bot.add_cog(restart(bot))





