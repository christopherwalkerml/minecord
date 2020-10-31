# bot.py
import src.utility.Global as Global

import discord,os
from src.managers.ChatManager import messageHandler

dir = os.path.dirname(os.path.realpath(__file__))

@Global.client.event
async def on_ready():
    print("Minecord has booted up!")
    await Global.client.change_presence(activity=discord.Game("type m!help for info"))

@Global.client.event
async def on_message(message):
    await messageHandler(message)


file = open(dir + "\\token.txt", "r")
token = file.readline().strip()

Global.client.run(token)