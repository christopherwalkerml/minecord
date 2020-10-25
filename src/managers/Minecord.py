# bot.py
import discord,os
from src.managers.MessageHandler import messageHandler

dir = os.path.dirname(os.path.realpath(__file__))
client = discord.Client()

@client.event
async def on_ready():
    print("Minecord has booted up!")
    await client.change_presence(activity=discord.Game("type m!help for info"))

@client.event
async def on_message(message):
    await messageHandler(message)


file = open(dir + "\\token.txt", "r")
token = file.readline().strip()

client.run(token)