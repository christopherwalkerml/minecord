from .Loot import Loot

class LootOre(Loot):

    def __init__(self, chance, rarity, loot_table, key_table):
        Loot.__init__(self, chance, rarity, loot_table, key_table)
        self.command = "mine"
        self.type = "ore"
        self.src = "../../images/ores/"
