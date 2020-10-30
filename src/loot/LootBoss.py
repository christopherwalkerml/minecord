from .Loot import *

import discord
from math import floor

class LootBoss(Loot):

    def __init__(self, chance, rarity, url, loot_table, key_table, health):
        self.health = health
        self.maxhealth = health
        Loot.__init__(self, chance, rarity, url, loot_table, key_table, "attack", "boss")

    def getHealthString(self):
        percent = floor((self.health / self.maxhealth) * 10)
        hstr = ""
        for i in range(percent):
            hstr += ":red_square:"

        for i in range(10 - percent):
            hstr += ":white_large_square:"

        return hstr

    def generate(self):
        self.health = self.maxhealth
        self.rolled_key = self.getKey()

    async def sendLoot(self):
        embed = self.createEmbed(self.rarity.capitalize() + " " + self.type + " has appeared", "Type `" + Global.prefix + self.command + " " + self.rolled_key + "` to get it")
        embed.add_field(name=f"Health - {floor((self.health / self.maxhealth) * 10)}", value=self.getHealthString(), inline=False)
        self.sent_message = await getRandomChannel().send(embed=embed)

    async def updateLoot(self, message_author):
        if len(self.contributors) == 0 or self.contributors[-1].userId != message_author.userId:
            self.contributors.append(message_author)

            self.health -= 1

            if self.health == 0:
                await self.dropLoot()
                return

            embed = self.createEmbed(self.rarity.capitalize() + " " + self.type + " has appeared", "Type `" + Global.prefix + self.command + " " + self.rolled_key + "` to attack it")
            embed.add_field(name=f"Health - {floor((self.health / self.maxhealth) * 10)}", value=self.getHealthString(), inline=False)
            await self.sent_message.edit(embed=embed)
        else:
            embed = self.createEmbed(self.rarity.capitalize() + " " + self.type + " has appeared", "Type `" + Global.prefix + self.command + " " + self.rolled_key + "` to attack it")
            embed.add_field(name=f"Health - {floor((self.health / self.maxhealth) * 10)}", value=self.getHealthString(), inline=False)
            embed.set_footer(text="You cannot attack twice in a row!")
            await self.sent_message.edit(embed=embed)

    async def dropLoot(self):
        Global.watcher.currentLoot = None

        embed = discord.Embed()
        embed.set_thumbnail(url=self.url)
        embed.title = "The " + self.rarity + " boss has been defeated!"

        # This generates a bunch of random items for each user that attacked the boss, and aggregates it by item type
        total_items = {}
        for u in self.contributors:
            if u.userId not in total_items: # add users to dict
                total_items[u.userId] = {}

            items = self.getItems()
            u.giveItems(items)

            for i in items: # generate items
                if i.item.name in total_items[u.userId]: #aggregate items
                    total_items[u.userId][i.item.name] += i.count
                else:
                    total_items[u.userId][i.item.name] = i.count

        for u in total_items:
            items = ""
            for i in total_items[u]:
                items += "- `" + str(total_items[u][i]) + " " + i + "`\n"

            embed.add_field(name=getUserFromId(u), value=items)

        await self.sent_message.edit(embed=embed)
