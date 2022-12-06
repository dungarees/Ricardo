import discord
from discord.ext import commands
from colorama import Fore, init


class poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Fore.LIGHTGREEN_EX}   [+]   Poll command is ready')  
        
    @commands.command()
    async def poll(self, ctx, opt1, opt2):
        message = await ctx.send("Pong!")
        await message.add_reaction('❎')
        await message.add_reaction('✅')
        
        
async def setup(bot):
    await bot.add_cog(poll(bot))
        
    