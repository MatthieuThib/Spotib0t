import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
SPOTIB0T_TOKEN = os.environ.get("TOKEN")
DEFAULTS_INTENTS = discord.Intents.default()
DEFAULTS_INTENTS.members = True 
PREFIX_COMMAND = "$"

bot = commands.Bot(
    command_prefix = PREFIX_COMMAND, 
    intents = DEFAULTS_INTENTS)


@bot.event
async def on_ready():
    print(" Spotib0t ready 🎵 ")
    
@bot.event
async def on_message(message):
    print(message.content)
    await bot.process_commands(message)
    print("end")
    #await message.channel.send(message.content)
    
@bot.command(name='delete', aliases=['del', 'd'])
async def delete(context, number: int):
    print('ici')
    messages = await context.channel.history(limit=number + 1).flatten()
    for each_message in messages:
        print(each_message)
        await each_message.delete()
    
bot.run(SPOTIB0T_TOKEN)