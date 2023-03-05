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

@client.command
async def classic(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
    	channel = ctx.author.voice.channel
    	await channel.connect()
        await client.voice_clients[0].disconnect()
    ch = client.get_channel(1071032500064882788)
        await ch.send ("123")
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
