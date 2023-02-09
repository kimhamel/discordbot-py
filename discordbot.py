from cmath import log
from distutils.sysconfig import PREFIX
import discord
import ui
from discord.ext import commands
import os

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    
@client.event
async def on_message(message):
    await message.add_reaction("🇭")
    await message.add_reaction("🇺")
    await message.add_reaction("🇹")
    await message.add_reaction("🇦")
    await message.add_reaction("🇴")
    await message.add_reaction("🦋")

class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="버튼", style=discord.ButtonStyle.grey)
    async def menu1(self, button, interaction):
        await interaction.response.send_message("잘하셨어요")

@client.command()
async def b(ctx):
    view = Menu()
    await ctx.send(view=view)    
    
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
