import src.utility.Global as Global

from random import randrange
import discord

class Loot:

    def __init__(self, chance, rarity, loot_table, key_table, command, ltype, path):
        self.chance = chance
        self.rarity = rarity
        self.loot_table = loot_table
        self.key_table = key_table

        self.generate()

        self.sent_message = None

        self.command = command
        self.type = ltype
        self.src = path

        self.contributors = []

    def getKey(self):
        return self.key_table[randrange(len(self.key_table))]

    def getItem(self):
        items = []

        for l in self.loot_table:
            if randrange(100) <= l["chance"]:
                items.append(l["item"])

        return [str(items.count(i)) + " " + i for i in set(items)]

    def generate(self):
        self.rolled_items = self.getItem()
        self.rolled_key = self.getKey()

    async def sendLoot(self):
        src = self.rarity + ".png"
        file = discord.File(self.src + src, filename=src)
        embed = discord.Embed()
        embed.add_field(name=src.replace(".png", "").capitalize() + " " + self.type + " has appeared", value="Type `" + Global.prefix + self.command + " " + self.rolled_key + "` to get it")
        embed.set_thumbnail(url="attachment://" + src)
        self.sent_message = await Global.channels[randrange(len(Global.channels))].send(file=file, embed=embed)

    async def updateLoot(self):
        items = ""
        for i in self.rolled_items:
            items += "- `" + i + "`\n"

        src = self.rarity + ".png"
        file = discord.File(self.src + src, filename=src)
        embed = discord.Embed()
        embed.add_field(name=self.contributors[0].name + " has collected " + self.rarity + " " + self.type, value=items)
        embed.set_thumbnail(url="attachment://" + src)
        await self.sent_message.delete()
        await Global.channels[randrange(len(Global.channels))].send(file=file, embed=embed)

