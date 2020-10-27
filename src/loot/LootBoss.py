from .Loot import *

class LootBoss(Loot):

    def __init__(self, chance, rarity, url, loot_table, key_table, health):
        Loot.__init__(self, chance, rarity, url, loot_table, key_table, "attack", "boss")
        self.health = health
        self.maxhealth = health

    def getHealthString(self):
        hstr = ""
        for i in range(self.health):
            hstr += ":red_square:"

        for i in range(self.maxhealth - self.health):
            hstr += ":white_large_square:"

        return hstr

    async def sendLoot(self):
        embed = self.createEmbed(self.rarity.capitalize() + " " + self.type + " has appeared", "Type `" + Global.prefix + self.command + " " + self.rolled_key + "` to get it")
        embed.add_field(name="Health", value=self.getHealthString(), inline=False)
        self.sent_message = await Global.channels[randrange(len(Global.channels))].send(embed=embed)

    async def updateLoot(self, message_author):
        if len(self.contributors) == 0 or self.contributors[-1].id != message_author.id:
            self.contributors.append(message_author)

            self.health -= 1

            if self.health == 0:
                await self.dropLoot()

            embed = self.createEmbed(self.rarity.capitalize() + " " + self.type + " has appeared", "Type `" + Global.prefix + self.command + " " + self.rolled_key + "` to get it\n" + self.getHealthString())
            await self.sent_message.edit(embed=embed)
        else:
            embed = self.createEmbed(self.rarity.capitalize() + " " + self.type + " has appeared", "Type `" + Global.prefix + self.command + " " + self.rolled_key + "` to get it\n" + self.getHealthString())
            embed.set_footer(text="You cannot attack twice in a row!")
            await self.sent_message.edit(embed=embed)

    async def dropLoot(self):
        # ADD TITLE, and add headers per user who got an attack in (sorted by most damage)

        items = ""
        for i in self.rolled_items:
            items += "- `" + i + "`\n"

        embed = self.createEmbed(self.contributors[0].name + " has collected " + self.rarity + " " + self.type, items)
        await self.sent_message.edit(embed=embed)

        Global.watcher.currentLoot = None
