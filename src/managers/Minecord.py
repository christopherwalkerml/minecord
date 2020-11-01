# bot.py
import src.utility.Global as Global

import discord,os
from src.managers.chatManager import messageHandler
from src.managers.reactionManager import reactionManager

dir = os.path.dirname(os.path.realpath(__file__))

@Global.client.event
async def on_ready():
    print("Minecord has booted up!")
    await Global.client.change_presence(activity=discord.Game("type m!help for info"))

@Global.client.event
async def on_message(message):
    await messageHandler(message)

@Global.client.event
async def on_reaction_add(reaction, user):
    await reactionManager(reaction, user)


file = open(dir + "\\token.txt", "r")
token = file.readline().strip()

Global.client.run(token)