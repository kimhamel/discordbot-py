from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

buttons = ButtonsClient(client)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_ready():
    DiscordComponents(bot, change_discord_methods=True)

@client.command()
await ctx.send(type=InteractionType.ChannelMessageWithSource, content="버튼", components=[Button(style=ButtonStyle.blue, label="호두이쁘니", custom_id="button")])

@client.event
async def on_button_click(interaction):
    if interaction.component.label.startswith("호두이쁘니"):
        await interaction.respond(type=InteractionType.ChannelMessageWithSource, content='Button Clicked')
        
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
