import os
import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Python files
from giphy_api import *
from spotify_api import *
from recommendation_system import *

# Set up environment variables
load_dotenv()
SPOTIB0T_TOKEN = os.environ.get("DISCORD_TOKEN")
API_GIPHY_TOKEN = os.environ.get("API_GIPHY_TOKEN")
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")

# Set up discord settings
DEFAULTS_INTENTS = discord.Intents.default()
DEFAULTS_INTENTS.members = True 
PREFIX_COMMAND = "$" 
     
# Instancing the bot and the spotify client
bot = commands.Bot(command_prefix = PREFIX_COMMAND, intents = DEFAULTS_INTENTS)
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

@bot.event
async def on_ready():
    print(" Spotib0t ready 🎵 ")
    
@bot.event
async def on_message(message):
    print("> ", message.content)
    # Ignore bot messages to prevent self-response
    if(message.author.bot == False and not message.content.lower().startswith(('$'))): 

        # Check if the message contains vulgarity
        if check_vulgarity(message):
            await message.channel.send("Mhm **" + message.author.name + "** , watch your language please ! 🤨🤯")
            message.content = ""

        # Check and respond to greetings
        elif message.content.lower().startswith(('hi','hello','good morning', 'good evening', 'hey','hola', 'yo', 'wesh')):
            await message.channel.send("Hey **" + message.author.name + " !** I'm **Spotibot** 😎. \nI'm your new best friend (yes I assure you 🐣).\nI love music on Spotify ! I know everything 🎧 \nWhat can I do for you ? 😁")

        # Check and respond to goodbye-like messages
        elif(re.search("(B|b)ye|(B|b)ye bye|(H|h)ave a nice day|(S|s)ayonara|(A|a)u revoir|(B|b)onne journée|(E|e)xit|(K|k)ill", message.content)):
            await message.channel.send("Bye **" + message.author.name + " !** \n See you soon 🐣") 
    
        # Analyse message and send a response
        else: 
            response = get_response(spotify, message.content)
            await message.channel.send(response)
       
    # Run bot commands if needed
    await bot.process_commands(message)
        
def check_vulgarity(message) :
    """ Check if the message contains bad words """
    words = message.content.split(" ")
    vulgarity = [True if element in ['fuck','bitch','fucking','motherfucker','shit', 'shut up', 'bastard', 'jerk'] else False for element in words]
    return True in vulgarity 
            
            
            
@bot.command(name = "join", aliases = ["j"]) 
async def join():
    bot.login(SPOTIB0T_TOKEN)
    
@bot.command(name='quit', aliases=['q'])
async def quit():
    bot.logout()
    
            
@bot.command(name='delete', aliases=['del', 'd'])
async def delete(context, number: int):
    messages = await context.channel.history(limit=number + 1).flatten()
    for message in messages:
        await message.delete()
         
@bot.command(name = "gif", aliases=['GIF','Gif'])
async def gif(context, name: str):
    gf = get_gifs_url(name, API_GIPHY_TOKEN)
    await context.channel.send(gf)
    
    
# Run Spotib0t
bot.run(SPOTIB0T_TOKEN)