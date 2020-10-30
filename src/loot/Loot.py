from src.loot.Item import Item
from src.utility.util import *

from random import randrange
import discord

class Loot:

    def __init__(self, chance, rarity, url, loot_table, key_table, command, ltype):
        self.chance = chance
        self.rarity = rarity
        self.url = url
        self.loot_table = loot_table
        self.key_table = key_table

        self.rolled_items = []
        self.rolled_key = "unknown"
        self.generate()

        self.sent_message = None

        self.command = command
        self.type = ltype

        self.contributors = []

    def getKey(self):
        return self.key_table[randrange(len(self.key_table))]

    def getItems(self):
        items = []

        for l in self.loot_table:
            roll = l.roll()
            items.append(roll) if roll is not None else None

        return items

    def generate(self):
        self.rolled_items = self.getItems()
        self.rolled_key = self.getKey()

    def createEmbed(self, name, value):
        embed = discord.Embed()
        embed.add_field(name=name, value=value)
        embed.set_thumbnail(url=self.url)
        return embed

    async def sendLoot(self):
        embed = self.createEmbed(self.rarity.capitalize() + " " + self.type + " has appeared", "Type `" + Global.prefix + self.command + " " + self.rolled_key + "` to get it")
        self.sent_message = await getRandomChannel().send(embed=embed)

    async def updateLoot(self, message_author):
        self.contributors.append(message_author)

        items = ""
        collection = None
        for i in self.rolled_items:
            emoji = Item.getEmoji(i.item.name)
            if Item.getCategory(i.item.name) == "collection":
                collection = i.item
            else:
                items += f"- {emoji} `{str(i.count)} {i.item.name}`\n"

        # collection items must always be at the end of the item report
        if collection is not None:
            emoji = Item.getEmoji(collection.name)
            items += f"- {emoji} ***`{collection.name}`***"

        user = getUserFromId(self.contributors[0].userId)
        self.contributors[0].giveItems(self.rolled_items)

        embed = self.createEmbed(str(user) + " has collected " + self.rarity + " " + self.type, items)
        embed.colour = self.contributors[0].cosmetic["colour"]
        await self.sent_message.edit(embed=embed)

        Global.watcher.currentLoot = None

    async def clearLoot(self):
        embed = self.createEmbed(self.rarity.capitalize() + " " + self.type + " has despawned", "You took to long to claim it!")
        await self.sent_message.edit(embed=embed)

        Global.watcher.currentLoot = None

