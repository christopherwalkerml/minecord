from .Loot import *

class LootBoss(Loot):

    def __init__(self, chance, rarity, loot_table, key_table, health):
        Loot.__init__(self, chance, rarity, loot_table, key_table, "attack", "boss", "../../images/bosses/")
        self.health = health

    async def sendLoot(self):
        src = self.rarity + ".png"
        file = discord.File(self.src + src, filename=src)
        embed = discord.Embed()
        embed.add_field(name=src.replace(".png", "").capitalize() + " " + self.type + " has appeared", value="Type `" + Global.prefix + self.command + " " + self.getKey() + "` to get it")
        embed.set_image(url="attachment://" + src)
        self.sent_message = await Global.channels[randrange(len(Global.channels))].send(file=file, embed=embed)
