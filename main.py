import asyncio
import os, sys
from dotenv import load_dotenv
import discord
from discord.ext import commands



#Import constants
from const import *



load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents = intents)
intents.members = True


TOKEN = os.getenv("TOKEN")






@bot.event
async def on_ready():
    os.system('title Ricardo')
    os.system('cls')
    print(banner)
    
    

#Loading cogs 
async def load():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            os.path.splitext(filename)
            index = filename.index('.')
            filename = filename[:index]
            await bot.load_extension(f'cogs.{filename}')
            
            
async def main():
    await load()
    await bot.start(TOKEN)
    
    
    

    
    


asyncio.run(main())




    




