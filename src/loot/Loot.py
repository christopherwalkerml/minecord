import src.utility.Global as Global

from random import randrange
import discord

class Loot:

    def __init__(self, chance, rarity, url, loot_table, key_table, command, ltype):
        self.chance = chance
        self.rarity = rarity
        self.url = url
        self.loot_table = loot_table
        self.key_table = key_table

        self.rolled_items = "unknown"
        self.rolled_key = "unknown"
        self.generate()

        self.sent_message = None

        self.command = command
        self.type = ltype

        self.contributors = []

    def getKey(self):
        return self.key_table[randrange(len(self.key_table))]

    def getItem(self):
        items = []

        for l in self.loot_table:
            for i in l["chance"]:
                if randrange(100) <= i:
                    items.append(l["item"])

        return [str(items.count(i)) + " " + i for i in set(items)]

    def generate(self):
        self.rolled_items = self.getItem()
        self.rolled_key = self.getKey()

    def createEmbed(self, name, value):
        embed = discord.Embed()
        embed.add_field(name=name, value=value)
        embed.set_thumbnail(url=self.url)
        return embed

    async def sendLoot(self):
        embed = self.createEmbed(self.rarity.capitalize() + " " + self.type + " has appeared", "Type `" + Global.prefix + self.command + " " + self.rolled_key + "` to get it")
        self.sent_message = await Global.channels[randrange(len(Global.channels))].send(embed=embed)

    async def updateLoot(self, message_author):
        self.contributors.append(message_author)

        items = ""
        for i in self.rolled_items:
            items += "- `" + i + "`\n"

        embed = self.createEmbed(self.contributors[0].name + " has collected " + self.rarity + " " + self.type, items)
        await self.sent_message.edit(embed=embed)

        Global.watcher.currentLoot = None

