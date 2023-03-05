from cmath import log
from distutils.sysconfig import PREFIX
import discord
from discord.ext import commands
import os

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    
@client.event
ch = client.get_channel()
if
    async def on_message(message):
        await message.add_reaction("🇼")
        await message.add_reaction("🇮")
        await message.add_reaction("🇫")
        await message.add_reaction("🇪")
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
