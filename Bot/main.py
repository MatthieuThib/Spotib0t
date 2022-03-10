import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

from giphy_api import get_gifs_url, get_random_gif

import re


load_dotenv()
SPOTIB0T_TOKEN = os.environ.get("TOKEN")
API_GIPHY_TOKEN = os.environ.get("API_GIPHY_TOKEN")
API_SPOTIFY_TOKEN = os.environ.get("API_SPOTIFY_TOKEN")
DEFAULTS_INTENTS = discord.Intents.default()
DEFAULTS_INTENTS.members = True 
PREFIX_COMMAND = "$"


bot = commands.Bot(command_prefix = PREFIX_COMMAND, intents = DEFAULTS_INTENTS)


@bot.event
async def on_ready():
    print(" Spotib0t ready 🎵 ")
    
@bot.event
async def on_message(message):
    
    if(message.author.bot != True):
        words = message.content.split(" ")

        vulgarity = [True if element in ['fuck','bitch','fucking','motherfucker','shit'] else False for element in words]
        print(message.content)

        if message.content.lower().startswith(('hi','hello','good morning', 'good evening', 'hey', 'wesh','hola')):
            await message.channel.send("Hey " + message.author.name + " ! I'm Spotibot 😎. \nI'm your new best friend (yes I assure you 🐣).\n I love music on Spotify ! I know everything 🎧 \nWhat can I do for you ? 😁")
        
        if True in vulgarity: 
            await message.channel.send("Mhm " + message.author.name + " , watch your language please ! 🤨🤯")
            message.content = ""

        elif re.match(r'\s(\\?\<artist>artist|singer|group)\ssing\s(\\?\<song>([a-zA-Z0-9]+\s)+)\\?', message.content) : 
            print('match')

                 
    await bot.process_commands(message)

    
@bot.command(name='delete', aliases=['del', 'd'])
async def delete(context, number: int):
    messages = await context.channel.history(limit=number + 1).flatten()
    for message in messages:
        await message.delete()
        
        
@bot.command(name = "gif", aliases=['GIF','Gif'])
async def gif(context, name: str):
    #if name is None:
    #    gf = get_random_gif(API_GIPHY_TOKEN)
    #else:
    #    gf = get_gifs_url(name, API_GIPHY_TOKEN)
    
    gf = get_gifs_url(name, API_GIPHY_TOKEN)
    await context.channel.send(gf)
     
        

    

bot.run(SPOTIB0T_TOKEN)