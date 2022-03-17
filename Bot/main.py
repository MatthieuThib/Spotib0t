import os
#import json

import discord
from discord.ext import commands

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


from giphy_api import *
from spotify_api import *

import re

from dotenv import load_dotenv
load_dotenv()
SPOTIB0T_TOKEN = os.environ.get("TOKEN")
API_GIPHY_TOKEN = os.environ.get("API_GIPHY_TOKEN")
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
DEFAULTS_INTENTS = discord.Intents.default()
DEFAULTS_INTENTS.members = True 
PREFIX_COMMAND = "$"

#async def verify_token():
#    if len(os.environ.get("API_SPOTIFY_TOKEN")) > 0:
#       return 'Valid Token ✅'
#    else: 
#       return 'Invalid Token ❌' 
        
        
bot = commands.Bot(command_prefix = PREFIX_COMMAND, intents = DEFAULTS_INTENTS)
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


@bot.event
async def on_ready():
    print(" Spotib0t ready 🎵 ")
    
@bot.event
async def on_message(message):
    if(message.author.bot != True): # Ignore bot messages

        print(" >", message.content)

        if check_vulgarity(message): 
            await message.channel.send("Mhm **" + message.author.name + "** , watch your language please ! 🤨🤯")
            message.content = ""

        elif message.content.lower().startswith(('hi','hello','good morning', 'good evening', 'hey', 'wesh','hola', 'yo', 'wesh')):
            await message.channel.send("Hey " + message.author.name + " ! I'm Spotibot 😎. \nI'm your new best friend (yes I assure you 🐣).\nI love music on Spotify ! I know everything 🎧 \nWhat can I do for you ? 😁")
            await message.channel.send("If you want to use **spotify** features, just copy past the following code in your browser : \nhttps://accounts.spotify.com/authorize?client_id=fe17030c83d54d098e9a70e4db39e2ab&scope=playlist-read-private&response_type=code&redirect_uri=https%3A%2F%2Fseb.com%2F")
            await message.channel.send("Enter **$token** followed by the link you were redirected to ")
            
        elif(re.search("(B|b)ye|(B|b)ye bye|(H|h)ave a nice day|(S|s)ayonara|(A|a)u revoir|(B|b)onne journée|(E|e)xit|(K|k)ill", message.content)):
            await message.channel.send("Bye !!")
        
        elif(message.content.lower().startswith(('$'))): # Ignore commands
            print(' > user command')
        
        else: 
            #r = get_response(spotify, message.content)
            #await message.channel.send(r)
            
            #await message.channel.send(get_artist_id(spotify, message.content))
            #await message.channel.send(get_top_n_tracks(spotify, message.content))
            await message.channel.send(get_n_related_artists(spotify, message.content))
            
       
    await bot.process_commands(message)
        

def check_vulgarity(message) :
    words = message.content.split(" ")
    vulgarity = [True if element in ['fuck','bitch','fucking','motherfucker','shit', 'shut up', 'bastard', 'jerk'] else False for element in words]
    return True in vulgarity 
            
@bot.command(name='delete', aliases=['del', 'd'])
async def delete(context, number: int):
    messages = await context.channel.history(limit=number + 1).flatten()
    for message in messages:
        await message.delete()
         
@bot.command(name='quit', aliases=['Quit', 'q', 'Q', 'stop', 'Stop'])
async def quit(context):
    bot.logout()
       
@bot.command(name = "gif", aliases=['GIF','Gif'])
async def gif(context, name: str):
    #if name is None:
    #    gf = get_random_gif(API_GIPHY_TOKEN)
    #else:
    #    gf = get_gifs_url(name, API_GIPHY_TOKEN)
    
    gf = get_gifs_url(name, API_GIPHY_TOKEN)
    await context.channel.send(gf)
    
    
bot.run(SPOTIB0T_TOKEN)