from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord_buttons_plugin import  *
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

buttons = ButtonsClient(client)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@bot.command()
async def 버튼(ctx):
    content = "호두 사진을 보낼것이라면 버튼을 눌러주세요.",
    channel = ctx.channel.id,
    components = [
        ActionRow([
            Button(
                label="권한",
                style=ButtonType().Primary,
                custom_id="button_one"
            )
        ])
    ]
    
@buttons.click
async def button_one(ctx):
    await ctx.reply("버튼이 눌렸습니다.")
    
@client.event
async def on_message(message):
    await message.add_reaction("🇭")
    await message.add_reaction("🇺")
    await message.add_reaction("🇹")
    await message.add_reaction("🇦")
    await message.add_reaction("🇴")
    await message.add_reaction("🦋")

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
